# Kế hoạch triển khai: Tổng hợp thông tin các dự án AI mã nguồn mở nổi bật

Kế hoạch này phác thảo các bước thu thập thông tin và tạo bảng tổng hợp chi tiết cho 5 dự án AI mã nguồn mở (open-source) từ lập trình viên Việt Nam trong Video 1 và dự án AI Agent cross-communication (giao tiếp chéo giữa các tác nhân) trong Video 2.

## Đề bài (User Requirement)
- Tổng hợp thông tin đầy đủ về các dự án AI được nhắc đến trong 2 video Facebook.
- Bao gồm: Link GitHub, mô tả chi tiết, gợi ý tình huống áp dụng hiệu quả, và cột ghi chú (notes) bổ sung.
- Lưu trữ kết quả dưới dạng tài liệu (artifact) trong thư mục `Research`.

## Hiện trạng (Current State)
- Đã tải thành công và trích xuất các khung hình (frames) từ Video 1 (`Top_5_du_an_AI_nguon_mo_noi_bat.mp4`).
- Thông qua việc kiểm tra hình ảnh từ các khung hình (frames), đã xác định được chính xác 5 dự án AI trong Video 1.
- Đã tải và đọc nội dung HTML của Video 2, xác định dự án liên quan đến kỹ năng giao tiếp chéo giữa Codex và Claude của tác giả Codeaholicguy.
- Đã tìm kiếm trên web để có đầy đủ thông tin chuẩn xác về đường dẫn GitHub, tính năng và bối cảnh sử dụng của cả 6 dự án này.

## Giải pháp kỹ thuật (Technical Solution)
1. **Dự án được phân tích**:
   - **Dự án 1 (Video 1)**: `ZuzooVn/machine-learning-for-software-engineers` (Lộ trình học Machine Learning từ trên xuống).
   - **Dự án 2 (Video 1)**: `vudovn/ag-kit` (Antigravity Kit - Bộ công cụ tối ưu hóa AI Agent cho Cursor/Windsurf).
   - **Dự án 3 (Video 1)**: `mrgoonie/claudekit-skills` (ClaudeKit - Hệ sinh thái kịch bản kỹ năng cho Claude Code).
   - **Dự án 4 (Video 1)**: `pnnbao97/VieNeu-TTS` (VieNeu-TTS - Mô hình chuyển văn bản thành giọng nói tiếng Việt/Anh chạy offline).
   - **Dự án 5 (Video 1)**: `truongduy2611/app-store-preflight-skills` (App Store Preflight - Quét lỗi vi phạm chính sách của Apple trước khi nộp ứng dụng).
   - **Dự án 6 (Video 2)**: `codeaholicguy/ai-devkit` (AI DevKit - Bộ công cụ chuẩn hóa quy trình phát triển và hỗ trợ giao tiếp chéo giữa các phiên làm việc của AI Agent).

2. **Cấu trúc lưu trữ**:
   - Tạo file tổng hợp tại: `C:\Users\vu.hoang\.gemini\antigravity\scratch\Research\Artifacts\open_source_ai_projects_summary.md`.
   - File sẽ trình bày dưới dạng bảng Markdown đầy đủ thông tin theo yêu cầu của người dùng.

## Các file bị ảnh hưởng (Affected Files)
- `[NEW]` [open_source_ai_projects_summary.md](file:///C:/Users/vu.hoang/.gemini/antigravity/scratch/Research/Artifacts/open_source_ai_projects_summary.md)

## Rủi ro tiềm ẩn & Lưu ý (Potential Risks & Notes)
- **Rủi ro**: Thông tin chi tiết của một số dự án có thể thay đổi theo thời gian (ví dụ: số lượng sao - stars trên GitHub).
- **Giải pháp**: Ghi rõ thời điểm thu thập dữ liệu (tháng 06/2026) và chỉ số stars gần đúng tại thời điểm đó để đảm bảo tính khách quan.

## Auditor Review
- Kính mời người kiểm duyệt (Auditor) rà soát cấu trúc bảng và các thông tin dự án đề xuất để đảm bảo độ chính xác trước khi thực hiện ghi file.
