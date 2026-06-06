# Kế hoạch triển khai: Phân tích video Facebook và tổng hợp Top 5 dự án AI nguồn mở

Tài liệu này mô tả kế hoạch tải video, phân tích nội dung, tìm kiếm thông tin chi tiết của 5 dự án AI `open source` (nguồn mở) được nhắc đến và lập bảng tổng hợp.

## Đề bài (Requirement)
- Phân tích video từ đường dẫn: `https://www.facebook.com/share/v/1CrxXpDmkh/`
- Trích xuất thông tin 5 dự án AI bao gồm: tên dự án, `link github` (đường dẫn kho chứa mã nguồn trên GitHub), mô tả chi tiết, `use case` (tình huống áp dụng hiệu quả) và ghi chú đi kèm.
- Lưu trữ kết quả tổng hợp vào thư mục `Research\Artifacts\`.

## Hiện trạng (Current State)
- Đã có một số file video tương tự trong `scratch` nhưng chưa được phân tích chính xác theo URL mới cung cấp.
- Cần tải hoặc lấy metadata từ URL Facebook để xác định danh sách dự án.

## Giải pháp kỹ thuật (Technical Solution)
1. **Tải/Lấy thông tin video:**
   - Sử dụng `yt-dlp` để tải hoặc trích xuất tiêu đề/nội dung của video từ đường dẫn Facebook được cung cấp vào thư mục `Research\downloads`.
   - Nếu bị chặn hoặc yêu cầu đăng nhập, sử dụng `fallback` (phương án dự phòng) là dùng `--cookies-from-browser chrome` hoặc tìm kiếm thông tin trực tiếp trên web theo tiêu đề video "Top 5 dự án AI nguồn mở nổi bật nhất của lập trình vis".
2. **Tìm kiếm thông tin dự án:**
   - Dựa trên danh sách 5 dự án trích xuất từ video, thực hiện tìm kiếm trên web để lấy link GitHub, tài liệu chính thức, và mô tả chi tiết của từng dự án.
3. **Tổng hợp thông tin:**
   - Lập bảng Markdown tổng hợp thông tin đầy đủ.
   - Ghi kết quả vào file `C:\Users\vu.hoang\.gemini\antigravity\scratch\Research\Artifacts\top_5_ai_open_source_projects.md`.

## Các file bị ảnh hưởng (Affected Files)
- `[NEW]` [top_5_ai_open_source_projects.md](file:///C:/Users/vu.hoang/.gemini/antigravity/scratch/Research/Artifacts/top_5_ai_open_source_projects.md) (File báo cáo tổng hợp)

## Rủi ro tiềm ẩn (Risks)
- **Lỗi tải video:** Facebook chặn tải tự động. *Biện pháp:* Sử dụng `cookies` trình duyệt Chrome hoặc tìm kiếm theo tiêu đề/kênh Facebook "lập trình vis" để thu thập danh sách dự án tương ứng.
- **Link GitHub thay đổi:** Một số dự án có thể đổi tên hoặc đường dẫn. *Biện pháp:* Tìm kiếm đường dẫn GitHub mới nhất của dự án.

## Kế hoạch kiểm chứng (Verification Plan)
- Đọc nội dung file báo cáo Markdown đã tạo và kiểm chứng các đường dẫn GitHub hoạt động chính xác.
