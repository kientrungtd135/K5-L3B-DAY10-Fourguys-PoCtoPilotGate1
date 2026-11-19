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

Chạy baseline và gate; đọc trace `T-002@55`; thêm cổng ghim chính sách hiệu lực, giới hạn hoàn theo tracking và trần khách, xác minh lỗi hãng theo kiện và trần lỗi/ngày, lọc trường gửi hãng theo allowlist, chặn hoàn khi policy check lỗi và chặn ghi hoàn lặp. Chốt checkpoint vòng 1 (`bfb563a4`), chạy prepared và gate; mọi ngưỡng đã ký đạt. Kiểm thử hồi quy 13/13 OK và thử lỗi LLM 429 xác nhận không fail-open, không ghi hoàn lặp. Có dùng AI để hỗ trợ phân tích trace và soạn cổng; tự kiểm tra kết quả eval, gate và test.

### Bằng chứng

Commit `19a1d0b`, `23e38d3`; checkpoint `bfb563a4`; runs `R-base-before-20261119-153634-4d2299`, `R-base-after-20261119-153910-8a1065`, `R-base-after-20261119-161308-fe1b1b`, `R-base-prepared-20261119-161437-fe1b1b`; Phiếu A A2/A5 và Phiếu B B0/B1/B5/B6 kỹ thuật/B7.1.

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

A1/A4 của Phiếu A; B3, lăng kính kinh doanh B6 và cơ sở chọn số B7.4 của Phiếu B; `demo-tv3.md`. Mã lần chạy sẽ bổ sung vào B8 và C12 khi có báo cáo.

### Exit ticket

Gợi ý để TV3 tự xác nhận sau lab: chi phí thấp mỗi lần gọi mô hình chưa bảo đảm pilot tiết kiệm; cần kiểm tra thêm chi phí chuyển duyệt giờ cao điểm và mức độ các số mô phỏng phản ánh tải thật.

## LuuNguyenChiDuc-2A202603923

### Phần việc phụ trách

Vận hành và pháp lý; phụ trách các mục `operations` và `legal` trong `config/operating_gates.json`, `submission/submission.json`, bảng thành viên trong `TEAM.md` và các mục được giao trong phiếu A/B/C.

### Đóng góp cụ thể

Điền sau khi hoàn thành.

### Bằng chứng

Điền mã commit, mã lần chạy (`runs/<mã>`) và mục phiếu sau khi hoàn thành.

### Exit ticket

Điền sau buổi lab.
