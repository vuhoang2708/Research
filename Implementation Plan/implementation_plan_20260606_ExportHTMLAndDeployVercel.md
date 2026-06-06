# Kế hoạch triển khai: Xuất bản HTML, tạo Repository và triển khai Vercel cho Dự án AI nguồn mở

Kế hoạch này phác thảo các bước xuất bản tài liệu tổng hợp thành trang web HTML đẹp mắt, tạo kho mã nguồn (repository) trên GitHub, đẩy mã nguồn lên và triển khai lên môi trường Live bằng Vercel.

## Đề bài (User Requirement)
- Xuất dữ liệu tổng hợp 6 dự án AI thành file HTML.
- Tạo repository và đẩy lên GitHub.
- Triển khai lên Vercel để lấy link trực tuyến (Vercel link).

## Hiện trạng (Current State)
- Đã có bảng tổng hợp Markdown tại `Research/Artifacts/open_source_ai_projects_summary.md`.
- Môi trường cục bộ có sẵn công cụ:
  - Git (`git`) điều khiển bởi git root cấp cha `C:\Users\vu.hoang\.gemini\antigravity`.
  - GitHub CLI (`gh`): `C:\Users\vu.hoang\.gemini\antigravity\scratch\tools\gh\bin\gh.exe`
  - Vercel CLI (`vercel`): phiên bản `54.4.1` đã cài đặt và chạy được lệnh.

## Giải pháp kỹ thuật (Technical Solution)

1. **Thiết kế trang HTML (`index.html`)**:
   - Vị trí: `C:\Users\vu.hoang\.gemini\antigravity\scratch\Research\index.html`.
   - **Giao diện**:
     - Áp dụng triết lý thiết kế cao cấp (Premium Design Aesthetics) với chế độ tối (dark mode) chủ đạo.
     - Sử dụng font chữ hiện đại (Outfit, Inter) từ Google Fonts.
     - Thiết kế theo phong cách kính mờ (glassmorphic cards) hiển thị thông tin 6 dự án AI.
     - Hiệu ứng di chuột (hover micro-animations): phóng to nhẹ thẻ, viền phát sáng neon (neon border-glow), chuyển tiếp mượt mà.
     - Các nhãn (badges) làm nổi bật số lượng `stars` (sao trên GitHub) và bối cảnh áp dụng.

2. **Quản lý Git & GitHub**:
   - Khởi tạo git repository riêng độc lập cho thư mục `Research` bằng cách chạy `git init` bên trong `Research`.
   - Tạo file `.gitignore` để loại bỏ các thư mục và tệp tin rác không cần đẩy lên GitHub:
     ```text
     /frames/
     *.mp4
     *.mp3
     .vercel/
     ```
   - Thực hiện `git add .` và `git commit -m "feat: init open source AI projects directory web"`.
   - Sử dụng GitHub CLI để tạo repository mới với chế độ công khai (public) và đẩy mã nguồn lên:
     ```powershell
     gh repo create vietnam-open-source-ai-projects --public --source=. --push
     ```

3. **Triển khai Vercel (Deployment)**:
   - Triển khai trang tĩnh HTML trực tiếp từ thư mục `Research` lên Vercel bằng lệnh:
     ```powershell
     vercel deploy --prod --yes
     ```
   - Ghi nhận đường dẫn liên kết (Vercel URL) của trang sản phẩm thực tế.

## Các file bị ảnh hưởng (Affected Files)
- `[NEW]` [index.html](file:///C:/Users/vu.hoang/.gemini/antigravity/scratch/Research/index.html)
- `[NEW]` [.gitignore](file:///C:/Users/vu.hoang/.gemini/antigravity/scratch/Research/.gitignore)
- `[NEW]` [walkthrough_20260606_ExportHTMLAndDeployVercel.md](file:///C:/Users/vu.hoang/.gemini/antigravity/scratch/Research/Artifacts/walkthrough_20260606_ExportHTMLAndDeployVercel.md)

## Rủi ro tiềm ẩn & Lưu ý (Potential Risks & Notes)
- **Rủi ro 1**: Xung đột Git khi khởi tạo git lồng nhau bên trong thư mục `C:\Users\vu.hoang\.gemini\antigravity`.
  - **Khắc phục**: Việc khởi tạo `.git` riêng trong thư mục `Research` là cần thiết để tạo repo độc lập cho Vercel. Chúng ta sẽ cấu hình loại trừ thư mục `Research/.git` ở repository cha hoặc bỏ qua nó để không làm bẩn working tree của repo cha.
- **Rủi ro 2**: Yêu cầu xác thực (interactive authentication) của GitHub CLI hoặc Vercel CLI có thể gây nghẽn tiến trình.
  - **Khắc phục**: Sử dụng các cờ tự động đồng ý (`--yes`, `--confirm`) và thực hiện từng bước kiểm tra. Nếu thiếu thông tin xác thực, sẽ hỗ trợ hướng dẫn người dùng kết nối.

## Auditor Review
- Kính mời Auditor rà soát tính hợp lý của phương án khởi tạo repo lồng và thiết kế UI trước khi tiến hành thực thi.
