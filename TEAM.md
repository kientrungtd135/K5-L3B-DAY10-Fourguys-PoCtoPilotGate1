# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Fourguys`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Fourguys-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trần Đức Trung | 2A202603938 | Kỹ sư cổng (trưởng nhóm) | Có |
|   2 | Dương Minh Chiến | 2A202603921 | Kỹ sư cổng (trace, test, chỉ số theo dõi) | Không |
|   3 | Trịnh Hưng Thịnh | 2A202603907 | Sản phẩm và kinh doanh | Không |
|   4 | Lưu Nguyễn Chí Đức | 2A202603923 | Vận hành và pháp lý | Không |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TranDucTrung-2A202603938

### Phần việc phụ trách

Kỹ sư cổng, trưởng nhóm; phụ trách `lab10/guards.py`, Git và các lệnh eval/gate/checkpoint/grade; các mục được giao trong phiếu A/B/C.

### Đóng góp cụ thể

Chạy baseline và gate; đọc trace `T-002@55`; thêm cổng ghim chính sách hiệu lực, giới hạn hoàn theo tracking và trần khách, xác minh lỗi hãng theo kiện và trần lỗi/ngày, lọc trường gửi hãng theo allowlist, chặn hoàn khi policy check lỗi và chặn ghi hoàn lặp. Chốt checkpoint vòng 1 (`bfb563a4`), chạy prepared và gate; mọi ngưỡng đã ký đạt. Với S7, chạy grade trước khi sửa và điền C0/C1; trace `S7-01@11`, `S7-04@11`, `S7-20@11` xác nhận allowlist chặn `customer_note` và `recipient_contact`, nên giữ cổng `notify_carrier`. Đối chiếu C6 của TV2, bổ sung nhánh thiếu người duyệt payload vào C1 và cập nhật C7 cho nhánh [1]+[2], đồng thời ghi rõ phần giám sát còn hở ở [3]. Sau khi TV2 hoàn tất C8/C9, chạy lại S7 after và base after: pass 1.0, không có PII/hoàn sai/lỗi hãng oan, không hồi quy; `customer_text_contact_rate` là 0.5 trên S7 và `carrier_payload_contact_rate` là 0. Grade sau C8/C9 đạt PASS-VISIBLE (integrity/criteria/visible/regression/monitor); máy không có hidden tests. Kiểm thử hồi quy 13/13 OK và thử lỗi LLM 429 xác nhận không fail-open, không ghi hoàn lặp. Có dùng AI để hỗ trợ phân tích trace và soạn cổng; tự kiểm tra kết quả eval, gate và test.

### Bằng chứng

Commit `19a1d0b`, `23e38d3`, `0217571`, `8dd64dc`, `8917325`, `8d1c19d`; checkpoint `bfb563a4`; runs `R-base-before-20261119-153634-4d2299`, `R-base-after-20261119-153910-8a1065`, `R-base-after-20261119-161308-fe1b1b`, `R-base-prepared-20261119-161437-fe1b1b`, `R-S7-grade-20261119-163314-5d2989`, `R-S7-after-20261119-165032-fe1b1b`, `R-base-after-20261119-165032-fe1b1b`, `R-S7-after-20261119-170348-498db4`, `R-base-after-20261119-170405-498db4`, `R-S7-grade-20261119-170412-498db4`; Phiếu A A2/A5, Phiếu B B0/B1/B5/B6 kỹ thuật/B7.1/B8 và Phiếu C C0/C1/C7.

### Exit ticket

Điều học được: phải kiểm tra số ngày khách khai với tracking và tính lại quyền lợi từ chính sách hiệu lực trước khi ghi tiền hoặc quy lỗi hãng; lỗi LLM cũng phải đóng an toàn trước lệnh ghi. Còn chưa chắc: cách xử lý khi tracking production bị thiếu/cập nhật trễ và dữ liệu sổ cái thiếu ngày mà không chuyển nhầm ca hợp lệ sang người duyệt.

## DuongMinhChien-2A202603921

### Phần việc phụ trách

Kỹ sư cổng (trace, test, chỉ số theo dõi); phụ trách `lab10/monitors.py` và các mục được giao trong phiếu A/B/C.

### Đóng góp cụ thể

Điền sau khi hoàn thành.

### Bằng chứng

Điền mã commit, mã lần chạy (`runs/<mã>`) và mục phiếu sau khi hoàn thành.

### Exit ticket

Điền sau buổi lab.

## TrinhHungThinh-2A202603907

### Phần việc phụ trách

Sản phẩm và kinh doanh; phụ trách `config/acceptance_criteria.json`, mục `business` trong `config/operating_gates.json` và các mục được giao trong phiếu A/B/C.

### Đóng góp cụ thể

Soạn mục tiêu cấp hệ thống, ngưỡng và quy tắc quyết định Gate 1, bản đồ dữ liệu và ví dụ thay đổi chính sách. Chọn phạm vi HN/HCM, ngân sách hoàn tự động và giới hạn chi phí dựa trên dữ liệu mô phỏng. Có dùng AI để đọc repo, hỗ trợ soạn phiếu, chọn ngưỡng và chuẩn bị demo.

### Bằng chứng

A1/A4 của Phiếu A; B3, B6 kinh doanh, B7.4/B8 của Phiếu B; C3.3/C5/C12 của Phiếu C; `demo-tv3.md`. V1 dựa trên `R-base-prepared-20261119-161437-fe1b1b`, v2 dựa trên `R-S7-grade-20261119-170259-5993e2`.

### Exit ticket

Điều rút ra: cần đọc chi phí toàn luồng cùng độ phủ và tải duyệt trước khi mở pilot. Điều còn cần kiểm tra: tải duyệt giờ cao điểm và payload các hãng thực nhận có giống mô phỏng hay không.

## LuuNguyenChiDuc-2A202603923

### Phần việc phụ trách

Vận hành và pháp lý; phụ trách các mục `operations` và `legal` trong `config/operating_gates.json`, `submission/submission.json`, bảng thành viên trong `TEAM.md` và các mục được giao trong phiếu A/B/C.

### Đóng góp cụ thể

Vòng 1: đặt mục `operations` và `legal` trong `config/operating_gates.json` (người chịu trách nhiệm `NV-TUNG`, người duyệt `NV-HANH`, 1 người trực, 6 ca mỗi giờ, chờ tối đa 60 phút, 5 điều kiện dừng, kiểm mẫu 10%, ghi chú giải thích bật; chặn `recipient_contact` và `customer_note` khi gửi hãng, chỉ ghi lỗi hãng khi tracking có nguyên nhân).
Viết runbook phần 1–3 và mục Giờ cao điểm (B7.5, B7.6) khớp các con số đó.
Viết HAZOP vòng 1 trên `notify_carrier` (B4, 5 dòng kỹ thuật và 2 dòng ngoài kỹ thuật) và checklist 9 nhóm việc có PIC (B5).
Phát hiện và báo cho Kỹ sư cổng hai chỗ chưa có cổng: trần 2 lỗi hãng mỗi ngày và các đường ghi hoàn khi LLM lỗi.

Vòng 2 (thẻ S7): viết HAZOP của thẻ (C4, 4 dòng, trong đó 2 nhánh chưa thấy trên trace), Risk register (C10, 3 dòng), cập nhật checklist và runbook phần 4–5 (C11), và điền `submission/submission.json`.

Dùng AI: dùng Claude Code để đọc code và dữ liệu, chạy trace và đánh giá, và soạn nháp các mục trên; số liệu và con số cấu hình được kiểm lại bằng lần chạy thực tế trước khi ghi vào phiếu.

### Bằng chứng

Commit `a3a80ac` (cấu hình operations, legal, B7.5, B7.6), `381eb51` (B4, B5), `3e62c98` (C4), `d901898` (C10, C11, `submission.json`).
Lần chạy: bộ nền `R-base-after-20261119-153910-8a1065` (cổng vòng 1), thẻ S7 `R-S7-before-20261119-163314-5d2989` và `R-S7-grade-20261119-170259-5993e2` (30 lần lộ PII ở mốc base, 0 ở prepared và after).
Phiếu B mục B4, B5, B7.5, B7.6; Phiếu C mục C4, C10, C11; trace `S7-01`, `S7-04`, `S7-05`, `S7-20`, `S7-21` ở seed 11 và `--adhoc` trên đơn quà tặng `O-1026`.

### Exit ticket

Điều học được: cổng lọc dữ liệu gửi hãng hoạt động theo **tên trường**, nên ghi `"phone"` hay `"name"` vào danh sách chặn thì không chặn được gì; phải chặn đúng khoá `recipient_contact` và `customer_note`. Và một cổng đang chạy tốt có thể khiến mọi chỉ số đầu ra bằng 0, nên cần thêm chỉ số cho thấy cổng có đang phải làm việc hay không.
Còn chưa chắc: các hệ thống trung gian của hãng có tuân theo hợp đồng bốn trường hay không, và liệu 1 người duyệt cùng kiểm mẫu 10% còn đủ khi chính sách `REFUND-v4` hạ hạn mức tự động xuống 100.000đ từ ngày 01/12/2026.
