"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _effective_policy(ctx):
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def pre_guard(ctx):
    policy = _effective_policy(ctx)
    if policy is None:
        return Verdict.escalate("không tìm thấy chính sách hoàn tiền có hiệu lực")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        policy = _effective_policy(ctx)
        if order is None or policy is None:
            return Verdict.escalate("thiếu đơn hàng hoặc chính sách hiệu lực để kiểm tra khoản hoàn")
        if order.get("customer_id") != ctx.ticket.get("customer_id"):
            return Verdict.escalate("người gửi không khớp chủ đơn")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        cause = parcel.get("delay_cause") or ("CARRIER" if delay > 0 else None)
        entitlement = H.entitlement_vnd(policy, order, delay, cause)
        requested = int(action.get("amount_vnd", 0))
        if requested > entitlement:
            ctx.log("refund_entitlement_cap", requested_vnd=requested, allowed_vnd=entitlement)
            if entitlement <= 0:
                return Verdict.deny("tracking và chính sách không cho phép khoản hoàn này")
            return Verdict.modify(
                "giới hạn khoản hoàn theo tracking và chính sách hiệu lực",
                amount_vnd=entitlement,
                payer="LOGIX",
                basis="policy",
            )

    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        policy = _effective_policy(ctx)
        if order is None or policy is None:
            return Verdict.deny("thiếu đơn hàng hoặc chính sách để xác minh lỗi hãng")
        parcel = next(
            (p for p in order.get("parcels", []) if p.get("parcel_id") == action.get("parcel_id")),
            None,
        )
        if parcel is None:
            return Verdict.deny("không tìm thấy kiện hàng trong dữ liệu tracking")
        delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking không xác nhận hãng có lỗi theo chính sách")
        if ctx.gates.get("legal", {}).get("carrier_fault_requires_recorded_cause") \
                and not parcel.get("delay_cause"):
            return Verdict.deny("thiếu nguyên nhân trễ được ghi nhận")
        changes = {}
        if action.get("carrier_id") != parcel.get("carrier_id"):
            changes["carrier_id"] = parcel.get("carrier_id")
        if action.get("delay_days") != delay:
            changes["delay_days"] = delay
        if changes:
            return Verdict.modify("dùng hãng và độ trễ theo kiện trong tracking", **changes)

    if tool == "notify_carrier":
        policy = _effective_policy(ctx)
        if policy is None:
            return Verdict.escalate("không xác định được trường dữ liệu được phép gửi hãng")
        payload = action.get("payload")
        if not isinstance(payload, dict):
            return Verdict.deny("payload gửi hãng không hợp lệ")
        allowed = set(policy.get("carrier_notice_fields") or [])
        blocked = set(ctx.gates.get("legal", {}).get("pii_fields_blocked_to_third_party") or [])
        filtered = {key: value for key, value in payload.items() if key in allowed and key not in blocked}
        if filtered != payload:
            ctx.log("carrier_payload_filtered", dropped_fields=sorted(set(payload) - set(filtered)))
            return Verdict.modify("chỉ gửi các trường được chính sách cho phép", payload=filtered)

    return Verdict.allow()
