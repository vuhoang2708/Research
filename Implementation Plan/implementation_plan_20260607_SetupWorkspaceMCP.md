# 📝 KẾ HOẠCH TRIỂN KHAI / IMPLEMENTATION PLAN
**Tên file**: `implementation_plan_20260607_SetupWorkspaceMCP.md`  
**Ngày tạo**: 07/06/2026  
**Dự án**: Research (Cấu hình Workspace MCP cho Antigravity)  
**Tác giả**: Antigravity Agent  

---

## 1. ĐỀ BÀI (REQUIREMENTS)
* Cài đặt và cấu hình đầy đủ `workspace-mcp` (Model Context Protocol server của Google Workspace) để Antigravity có thể gọi các dịch vụ Gmail, Drive, Docs, Sheets, Calendar...

---

## 2. GIẢI PHÁP KỸ THUẬT (TECHNICAL SOLUTION)
1. **Thêm server vào `mcp_config.json`**:
   * Sửa tệp cấu hình toàn cục `C:\Users\vu.hoang\.gemini\antigravity\mcp_config.json`.
   * Thêm cấu hình khởi chạy `workspace-mcp` qua `uvx` ở dạng Stdio Server.
2. **Cung cấp biến môi trường (Environment Variables)**:
   * Do OAuth yêu cầu Client ID và Client Secret từ tài khoản Google Cloud của anh, tôi sẽ cấu hình sẵn các biến môi trường này dưới dạng placeholder trong `mcp_config.json`:
     - `GOOGLE_OAUTH_CLIENT_ID`: `"NHẬP_CLIENT_ID_CỦA_ANH_VÀO_ĐÂY"`
     - `GOOGLE_OAUTH_CLIENT_SECRET`: `"NHẬP_CLIENT_SECRET_CỦA_ANH_VÀO_ĐÂY"`
   * Anh chỉ cần điền đúng mã Client ID & Secret vào là hệ thống sẽ tự động kích hoạt trình duyệt đăng nhập khi gọi lệnh đầu tiên.

---

## 3. FILE BỊ ẢNH HƯỞNG (AFFECTED FILES)
* `C:\Users\vu.hoang\.gemini\antigravity\mcp_config.json`

---

## 4. AUDITOR REVIEW (ĐÁNH GIÁ CỦA ANH VŨ)
* Vui lòng duyệt nhanh bằng cách phản hồi **Approve**, **Đồng ý** hoặc **OK** để tôi tiến hành ghi file cấu hình ngay lập tức!
