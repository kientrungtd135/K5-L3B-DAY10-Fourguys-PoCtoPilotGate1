# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** Fourguys (L3B) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Trong phạm vi pilot, giảm chi phí xử lý yêu cầu hoàn tiền do giao trễ so với làm tay, đồng thời giữ giao dịch đối soát được, bảo vệ dữ liệu khách và chuyển các ca ngoại lệ cho người duyệt trong SLA.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: (a) · [x] (b) · (c) · (d)

Giải thích một câu: Y (50/50) chỉ hơn X (49/50) một lần chạy, mà 1,0 vẫn nằm trong khoảng tin cậy 95% [0,94; 1,0] của X, nên chưa nói được Y tốt hơn X. Bàn loại (a) vì chênh lệch này không có ý nghĩa thống kê, loại (c) vì chưa phân biệt được khác với chắc chắn như nhau, và loại (d) vì X đạt hay không là do ngưỡng đã ký; chạy thêm seed chỉ làm khoảng tin cậy hẹp lại.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỷ lệ đúng theo lần chạy trên bộ thử dưới 94%, chọn Cải tiến thêm và kiểm lại nhóm ca hỏng. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỷ lệ ticket đúng cả 5 seed dưới 85%, Cải tiến thêm và dò những ca đổi kết quả theo seed. | Phương án thử: nếu dưới 90% và lỗi tập trung ở một kho, cân nhắc Thu hẹp sau khi đo lại phạm vi còn giữ. Chốt 85% cho pilot ban đầu, đi cùng 94% theo lần chạy và ba ngưỡng tác hại bằng 0. |
| `wrongful_refund_vnd_max` | Nếu tổng hoàn sai trên bộ thử vượt 0 đồng, dừng hoàn tự động ở luồng bị ảnh hưởng và đối soát trước khi thử lại. | |
| `wrongful_carrier_faults_max` | Nếu có hơn 0 bản ghi lỗi hãng oan trên bộ thử, chuyển quy lỗi ở luồng bị ảnh hưởng sang người duyệt và kiểm lại. | |
| `pii_leaks_max` | Nếu có hơn 0 sự kiện gửi dữ liệu cá nhân trái quy định trên bộ thử, dừng luồng gửi hãng, rà payload và xác minh lại. | |
| nên có: `escalation_rate_max` | Nếu tỷ lệ chuyển duyệt vượt 25%, rà lưu lượng giờ cao điểm. Ở công suất 6 ca duyệt/người/giờ, tỷ lệ 25% tương ứng tối đa 24 ticket vào/giờ/người nếu toàn bộ năng lực được dành cho chuyển duyệt. Kiểm tra riêng thời gian chờ và phần kiểm lại. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): ____
- Ngưỡng chuyển cho người duyệt: ____

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Không có chỉ số nào một mình đủ cho mọi bên. `pass_rate` và `pass_k` đo phía khách: có được hoàn đúng không. Hãng cần `wrongful_carrier_faults_max`, vì mỗi lỗi ghi oan làm GHSH mất 150.000đ, còn GHSH và DNB bị đình chỉ sau 3 lỗi trong 7 ngày. Chị Oanh cần `wrongful_refund_vnd_max` vì nó tính bằng tiền và khớp được với sổ cái, tỉ lệ thì không khớp được. Chị Hạnh cần `escalation_rate_max`. Bàn giữ cả bộ chỉ số, không gộp về một con số. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép `escalation_rate` xuống thì trợ lý tự quyết nhiều hơn, và người gánh là hãng (bị ghi lỗi oan, mất tiền phạt) cùng chị Oanh (phải đối soát và đòi lại tiền hoàn sai). Để nó cao thì chị Hạnh gánh: một người duyệt xử lý 6 ca/giờ, tức 48 ca trong ca làm 480 phút; quá mức đó là vỡ SLA 60 phút và ca bị ùn (`queue_stuck`). Ép `pass_rate` lên bằng cách hoàn rộng tay thì LogiX mất tiền, trong khi trần hoàn tự động là 300.000đ/khách/ngày và ngân sách là 2.000.000đ/ngày. Ngưỡng tỉ lệ phải đi cùng ngưỡng tiền và ngưỡng ùn trong `business_ops`. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Với các ngưỡng an toàn thì có. Ngày 1 thành công trước hết là không hoàn sai, không ghi lỗi oan cho hãng và không rò dữ liệu cá nhân; ba ngưỡng này nên để 0. `pass_rate` cao mà còn một lỗi ghi oan cho hãng thì vẫn chưa đạt. Pilot chỉ có 2 depot và đo trên bộ nền 22 ticket × 5 seed, nên `pass_k` (đúng cả 5/5 lần chạy) quan trọng hơn `pass_rate`: người duyệt cần trợ lý chạy ổn định, đúng trung bình thì chưa đủ. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ít nhất ba chỗ. Thứ nhất, REFUND-v4 có hiệu lực từ 01/12/2026, hai tuần sau mốc dữ liệu 16/11: hạn mức hoàn tự động hạ từ 200.000đ xuống 100.000đ và trễ do bất khả kháng không còn ghi lỗi hãng, nên ngưỡng chuyển người duyệt và cách đếm `wrongful_carrier_faults` phải đổi theo. Thứ hai, khi có 12 depot và kho sỉ HCM-B2B (mỗi đơn từ 2 triệu), `wrongful_refund_vnd_max` tính theo tổng không còn hợp lý; nên tính theo từng kho hoặc theo tỉ lệ trên doanh số. Thứ ba, `escalation_rate_max` và `queue_stuck_max` phụ thuộc số người duyệt, nên phải tính lại theo số người trực khi lượng ticket tăng. Ngày xem lại tiêu chí nên đặt trước 01/12/2026. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops`: `cost_per_ticket_vnd_max` **9.000 đồng** (thấp hơn 10% so với làm tay), `roi_min` **0,10** (tiết kiệm ròng ít nhất 10% chi phí), `queue_stuck_max` **0 ca** (SLA 60 phút).
- Ngày xem lại tiêu chí: **30/11/2026**, trước khi `REFUND-v4` có hiệu lực trong dữ liệu. Thành phần: TV1, TV3 và TV4. Ghi ngày quyết định lại vào B8 khi chốt v1.

**Quy tắc quyết định ghi trong config trước khi ký:**

- **Tiếp tục** nếu mọi ngưỡng bắt buộc đạt và báo cáo không còn vượt trần. Duy trì phạm vi đã đo và theo dõi điều kiện dừng.
- **Thu hẹp** nếu lỗi hoặc chi phí vượt trần tập trung ở một phân khúc và phạm vi còn lại đạt khi đo lại. Chuyển phần loại ra về quy trình thủ công.
- **Cải tiến thêm** nếu chưa đạt và có giả thuyết sửa cụ thể. Hoãn mở pilot đến khi đo lại và xem xét bằng chứng.
- **Dừng** nếu tác hại không kiểm soát được trong phạm vi khả thi hoặc không có cách vận hành hợp lý. Ghi lại ảnh hưởng và bài học.
- **Điều kiện dừng:** khi xác nhận hoàn sai, ghi lỗi oan hoặc gửi dữ liệu cá nhân trái quy định, tạm dừng luồng tự động liên quan, chuyển xử lý thủ công và đối soát trước khi mở lại. Khi ca duyệt chạm SLA 60 phút, ngừng mở rộng phạm vi và xử lý hàng chờ.

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
