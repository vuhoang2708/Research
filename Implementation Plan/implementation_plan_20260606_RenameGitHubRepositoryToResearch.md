# Kế hoạch triển khai: Đổi tên GitHub Repository thành "Research"

Kế hoạch này phác thảo các bước đổi tên kho lưu trữ mã nguồn từ `vietnam-open-source-ai-projects` sang `Research` trên GitHub và cập nhật cấu hình điều khiển cục bộ.

## Đề bài (User Requirement)
- Đổi tên repository trên GitHub thành "Research".

## Hiện trạng (Current State)
- Repository hiện tại trên GitHub đang có tên là `vietnam-open-source-ai-projects` thuộc tài khoản `vuhoang2708`.
- Địa chỉ URL hiện tại: `https://github.com/vuhoang2708/vietnam-open-source-ai-projects`.
- Cấu hình remote `origin` cục bộ đang trỏ vào URL cũ.

## Giải pháp kỹ thuật (Technical Solution)

1. **Đổi tên trên GitHub**:
   - Sử dụng GitHub CLI để đổi tên từ thư mục cục bộ `Research`:
     ```powershell
     gh repo rename Research --yes
     ```
   - Lệnh này sẽ tự động thay đổi tên trên máy chủ GitHub và đồng thời cập nhật liên kết remote `origin` trong tệp cấu hình `.git/config` cục bộ của thư mục `Research`.

2. **Cập nhật Vercel (nếu cần thiết)**:
   - Do chúng ta đã kết nối Vercel với dự án thông qua GitHub, việc đổi tên repository có thể yêu cầu Vercel cập nhật liên kết. Chúng ta sẽ chạy lại lệnh triển khai Vercel hoặc kiểm tra xem Vercel có tự động nhận diện liên kết mới thông qua redirect không:
     ```powershell
     vercel deploy --prod --yes
     ```

## Các tệp tin bị ảnh hưởng (Affected Files)
- `[NEW]` [walkthrough_20260606_RenameGitHubRepositoryToResearch.md](file:///C:/Users/vu.hoang/.gemini/antigravity/scratch/Research/Artifacts/walkthrough_20260606_RenameGitHubRepositoryToResearch.md)

## Rủi ro tiềm ẩn & Lưu ý (Potential Risks & Notes)
- **Rủi ro**: Nếu tài khoản `vuhoang2708` đã có sẵn một kho lưu trữ khác tên là `Research`, lệnh đổi tên sẽ thất bại do trùng tên.
  - **Giải pháp**: Nếu gặp lỗi trùng tên, Agent sẽ báo lại cho người dùng và đề xuất hướng xử lý (ví dụ: xoá repo cũ trùng tên hoặc đổi sang tên khác như `Research-AI`).

## Auditor Review
- Kính mời Auditor xem xét phương án thực thi và xác nhận.
