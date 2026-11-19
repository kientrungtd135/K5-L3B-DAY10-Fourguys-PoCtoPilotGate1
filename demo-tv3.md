# Demo Gate 1 · TV3 (Sản phẩm và kinh doanh)

Phần TV3 chiếm khoảng 90 giây cuối trong demo 5 phút. Sau khi TV1 chiếu báo cáo ba mốc và TV2/TV4 trình bày bằng chứng kỹ thuật, vận hành, TV3 giải thích quyết định v1 → v2, phạm vi pilot và điều kiện xem xét lại.

## Lời thoại

> Trước khi nhận thẻ, nhóm chọn **[v1]** trên bộ nền ở mốc `prepared` **[mã lần chạy B8]**. Chỉ số **[chỉ số]** đạt **[giá trị]** so với ngưỡng đã ký **[ngưỡng]**. Phân khúc cần chú ý nhất là **[kho hoặc hãng]** vì **[chỉ số và giá trị]**.
>
> Trên thẻ **[Sx]**, **[chỉ số tác hại]** lần lượt là **[base] → [prepared] → [after]**. Cổng vòng 1 đã **[kết quả có số]**. Sau khi **[đổi cổng, phạm vi hoặc quy trình]**, chi phí là **[x] đồng/ticket** so với **10.000 đồng/ticket làm tay** trong mô phỏng. ROI là **[y]** so với ngưỡng **[z]**. **[Nêu trần hoặc ngưỡng còn vướng, hoặc xác nhận các điều kiện bắt buộc đều đạt theo báo cáo.]**
>
> Nhóm **[giữ/đổi]** quyết định thành **[v2]** vì **[con số quyết định và dòng `decision_rule`]**. **[Nêu phạm vi pilot và luồng xử lý phần nằm ngoài phạm vi, hoặc việc cần làm và hạn xem xét lại.]** Nếu có pilot thật, nhóm sẽ đo lại **[một chỉ số cụ thể]** vì **[giả định trong dữ liệu mô phỏng có thể sai]**.

## Số liệu cần đặt cạnh nhau trên màn hình

| Bằng chứng | Nguồn |
|---|---|
| v1, mã `prepared` và ngưỡng quyết định | B8 của [Phiếu B](templates/form-b-evaluation-gates.md), đối chiếu [tiêu chí đã ký](config/acceptance_criteria.json). |
| Một chỉ số tác hại qua ba mốc của **cùng thẻ** | `runs/grade-report.md` hoặc bản gom `submission/runs/grade-report.md`. Ghi cả ba mã vào C12. |
| Chi phí mỗi ticket, ROI, hàng chờ, độ phủ và kho/hãng xấu nhất | Report `after` và mục `by_segment` trong `report.json`. Khi viện dẫn, đọc giá trị thực tế cùng ngưỡng đã ký hoặc trần vận hành tương ứng. |
| v2, lý do giữ/đổi, phạm vi và ba dòng bắt buộc | C12 của [Phiếu C](templates/form-c-incident.md). TV4 chép ba dòng sang `submission/submission.json`. |

Nếu còn vượt trần hoặc còn ngưỡng đã ký chưa đạt, chọn giữa **Thu hẹp**, **Cải tiến thêm** và **Dừng** theo `decision_rule` và bằng chứng. Với **Thu hẹp**, nêu kho/phần trăm được giữ, số người trực và nơi chuyển ticket bị loại. Với **Cải tiến thêm**, nêu nhánh lỗi sẽ xử lý và hạn đo lại. Với **Dừng**, nêu bằng chứng và bài học sẽ ghi lại.

## Số liệu gốc để trả lời phản biện

Các con số dưới đây lấy từ `ops_limits` và `ops_facts` trong [world.json](data/world.json). Giá trị nhóm chọn cho B7.4 cần có lý do riêng.

- Finance đặt ngân sách hoàn **tự động** tối đa **2.000.000 đồng/ngày**. Khi tổng hoàn tự động cho một khách vượt **300.000 đồng/ngày**, cần phê duyệt.
- Làm tay hoặc xử lý một ca chuyển duyệt tốn **10.000 đồng/ticket**. Trần **chi phí LLM** là **1.500 đồng/ticket**. Chi phí mỗi ticket trong báo cáo còn phản ánh chi phí xử lý của con người.
- Một người duyệt xử lý **6 ca/giờ**, SLA nhận xử lý là **60 phút**. Mỗi người trực thêm tốn **30.000 đồng/ca**. Khi đổi số người trực, đọc lại cả hàng chờ và ROI.
- ROI bằng **tiết kiệm ròng chia cho chi phí**. Tiết kiệm ròng trừ cả chi phí vận hành và khoản hoàn sai khỏi chi phí làm tay lẽ ra phải bỏ ra.

## Việc TV3 cần chốt trước khi nói

- A1–A5 và tiêu chí chấp nhận do nhóm thống nhất trước lần đo đầu tiên. Ghi commit ký vào A5.
- B3, B7.4 và B8 lần lượt ghi bản đồ dữ liệu/drift, lý do chọn cổng kinh doanh và quyết định v1. Dùng kết quả bộ nền cho B8.
- C3 điền phần dành cho thẻ đã bốc nếu áp dụng. C12 dùng báo cáo thẻ và giữ nguyên v1 đã ghi trong B8. Ba dòng chốt nêu giả định môi trường, cổng giảm hay ngăn tác hại và điều cần đo lại khi chạy thật.
