# Demo Gate 1 · TV3 (Sản phẩm và kinh doanh)

Phần TV3 chiếm khoảng 90 giây cuối trong demo 5 phút. Sau khi TV1 chiếu báo cáo ba mốc và TV2/TV4 trình bày bằng chứng kỹ thuật, vận hành, TV3 giải thích quyết định v1 → v2, phạm vi pilot và điều kiện xem xét lại.

## Lời thoại

> Ở v1, nhóm chọn **Tiếp tục** trong hai kho HN và HCM. Bộ nền ở mốc `prepared` đạt 100% cả theo lần chạy và theo ticket đúng cả năm seed, so với ngưỡng 94% và 85%. Phạm vi đó gồm 13 trên 22 ticket bộ nền.
>
> Trên thẻ **S7**, số lần lộ dữ liệu là **30 → 0 → 0**. VNX có 15 lần ở `base`, giảm còn 0 ở `after` trong phạm vi đã đo. Cổng vòng 1 đã chặn các trường ngoài danh sách. Vòng 2 giữ cổng và bổ sung hai monitor để theo dõi thông tin liên hệ trong ticket và trong payload gửi hãng. Ở `after`, chi phí là **6.434 đồng/ticket** so với **10.000 đồng làm tay**, ROI **55%** so với ngưỡng **10%**, và **0 ca ùn**.
>
> V2 giữ **Tiếp tục** vì các ngưỡng đã ký đều đạt và báo cáo không còn vượt trần. Hai kho HN/HCM bao phủ 6 trên 8 ticket S7 với một người duyệt trực. Hai ticket còn lại chuyển xử lý thủ công. Trước Gate 2, nhóm sẽ đối soát payload ở cả đầu gửi và đầu nhận, vì hệ thống trung gian của hãng có thể xử lý các trường khác với mô phỏng.

Bằng chứng v1: `R-base-prepared-20261119-161437-fe1b1b`. Bằng chứng v2: `R-S7-grade-20261119-170412-498db4` (`PASS-VISIBLE`).

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
