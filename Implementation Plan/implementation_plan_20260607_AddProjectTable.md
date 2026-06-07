# 📝 KẾ HOẠCH TRIỂN KHAI / IMPLEMENTATION PLAN
**Tên file**: `implementation_plan_20260607_AddProjectTable.md`  
**Ngày tạo**: 07/06/2026  
**Dự án**: Research (Danh mục dự án AI mã nguồn mở)  
**Tác giả**: Antigravity Agent  

---

## 1. ĐỀ BÀI (REQUIREMENTS)
* Bổ sung một bảng thông tin dự án hoàn chỉnh ngay bên cạnh hoặc dưới danh sách thẻ hiện tại.
* Các cột của bảng phải bao gồm chính xác:
  1. **STT** (Số thứ tự)
  2. **Tên Repo** (Tên kho lưu trữ)
  3. **Link GitHub** (Đường dẫn GitHub)
  4. **Mục đích** (Mục đích sử dụng/mô tả ứng dụng)
  5. **Các ghi chú khác** (Ghi chú bổ sung dành cho nhà phát triển)
* Giao diện bảng phải được thiết kế cao cấp, đồng bộ với phong cách Glassmorphism của hệ thống và hiển thị trực quan thông tin.
* Thực hiện commit, push mã nguồn lên GitHub và cập nhật trực tiếp lên Vercel.

---

## 2. HIỆN TRẠNG (CURRENT STATE)
* **index.html hiện tại**: Có hệ thống toggle chuyển đổi ẩn/hiện giữa Card và Table, nhưng cột của Table chưa khớp 100% với tên gọi yêu cầu của anh Vũ (đang là: Tên dự án, Phân loại, Mô tả, Tình huống áp dụng, Ghi chú, Link).
* **Trạng thái Git**: Sạch sẽ sau lần push trước.

---

## 3. GIẢI PHÁP KỸ THUẬT (TECHNICAL SOLUTION)
* **Cải tiến HTML/CSS/JS**:
  * Chỉnh sửa cấu trúc bảng trong `index.html` để có chính xác 5 cột: STT, Tên Repo, Link GitHub, Mục đích, Các ghi chú khác.
  * Hiển thị song song cả hai chế độ: Dashboard kiểu Thẻ ở trên và Bảng dữ liệu chi tiết ở ngay dưới (hoặc sắp xếp bố cục tab rõ ràng hiển thị bảng chi tiết đầy đủ mặc định). Để tối ưu trải nghiệm, tôi sẽ hiển thị cả hai phần nối tiếp nhau trên cùng một trang, giúp người dùng cuộn xuống là thấy ngay bảng đối chiếu.
  * Đánh số thứ tự tự động (STT từ 1 đến 13) cho các dự án trong bảng.
  * Liên kết ô tìm kiếm chung để lọc dữ liệu đồng thời ở cả giao diện Thẻ và giao diện Bảng.
* **Đẩy mã nguồn (Push code)**:
  * Sau khi anh duyệt, tiến hành sửa file, commit và push lên GitHub `master`.
* **Deploy & Nghiệm thu**:
  * Chạy deploy lên Vercel.
  * Dùng browser tool kiểm chứng giao diện live và chụp ảnh báo cáo.

---

## 4. BẢN PHÁC THẢO BẢNG DỮ LIỆU (TABLE DATA SKETCH)

Bảng dữ liệu sẽ chứa đầy đủ 13 dự án với các cột:
1. **STT**: 1 - 13
2. **Tên Repo**: Tên dự án (ví dụ: OpenScreen)
3. **Link GitHub**: Dạng thẻ link bấm trực tiếp sang GitHub.
4. **Mục đích**: Tóm tắt công dụng chính + tình huống áp dụng.
5. **Các ghi chú khác**: Các lưu ý đặc thù về bảo mật, offline, cấu hình phần cứng.

---

## 5. RỦI RO & LƯU Ý
* Giữ nguyên thiết kế responsive để bảng tự động co giãn hoặc có thanh cuộn ngang trên thiết bị di động, tránh tràn vỡ khung giao diện.

---

## 6. AUDITOR REVIEW (ĐÁNH GIÁ CỦA ANH VŨ)
* Vui lòng phê duyệt kế hoạch. Sau khi anh gõ **Approve**, **Đồng ý** hoặc **OK**, tôi sẽ tiến hành cập nhật giao diện `index.html` và deploy lên Vercel.
