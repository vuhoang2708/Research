# 🧪 BÁO CÁO CẤU HÌNH & HƯỚNG DẪN NGHIỆM THU (UAT CONFIGURATION REPORT)
**Tên file**: `UAT_report_20260607_SetupWorkspaceMCP.md`  
**Ngày thực hiện**: 07/06/2026  
**Dự án**: Research (Cấu hình Workspace MCP cho Antigravity)  
**Tác giả**: Antigravity Agent  

---

## 1. TRẠNG THÁI CẤU HÌNH (CONFIGURATION STATE)
* **Tệp cấu hình**: [C:\Users\vu.hoang\.gemini\antigravity\mcp_config.json](file:///C:/Users/vu.hoang/.gemini/antigravity/mcp_config.json)
* **Nội dung cấu hình đã thêm**:
  ```json
  "workspace-mcp": {
    "command": "uvx",
    "args": [
      "workspace-mcp",
      "--tool-tier",
      "core"
    ],
    "env": {
      "GOOGLE_OAUTH_CLIENT_ID": "NHẬP_GOOGLE_OAUTH_CLIENT_ID_CỦA_ANH_TẠI_ĐÂY",
      "GOOGLE_OAUTH_CLIENT_SECRET": "NHẬP_GOOGLE_OAUTH_CLIENT_SECRET_CỦA_ANH_TẠI_ĐÂY"
    }
  }
  ```
* **Mức độ kiểm chứng**: `UNVERIFIED` (Chưa kiểm chứng do cần Client ID và Client Secret thực tế của người dùng).

---

## 2. HƯỚNG DẪN CHI TIẾT CÁCH LẤY THÔNG TIN XÁC THỰC OAUTH (GOOGLE CLOUD)
Để cấu hình hoạt động, anh vui lòng thực hiện các bước sau để lấy Client ID và Client Secret:

### Bước 2.1: Tạo dự án trên Google Cloud Console
1. Truy cập [Google Cloud Console](https://console.cloud.google.com/).
2. Đăng nhập bằng tài khoản Google (tài khoản Google Workspace của công ty hoặc Gmail cá nhân).
3. Nhấp vào menu chọn dự án ở góc trên bên trái -> Chọn **New Project**.
4. Điền tên dự án (ví dụ: `Workspace-MCP-Antigravity`) -> Nhấn **Create**.

### Bước 2.2: Thiết lập màn hình đồng ý OAuth (OAuth Consent Screen)
1. Vào menu bên trái -> Chọn **APIs & Services** -> **OAuth consent screen**.
2. Chọn **User Type**:
   * **Internal**: Nếu anh dùng tài khoản Google Workspace doanh nghiệp (không cần Google duyệt app).
   * **External**: Nếu anh dùng tài khoản Gmail cá nhân (cần cấu hình Test Users).
3. Nhấn **Create**.
4. Điền các thông tin bắt buộc:
   * **App name**: `Workspace MCP`
   * **User support email**: Email của anh.
   * **Developer contact information**: Email của anh.
5. Nhấn **Save and Continue** qua các bước tiếp theo.
6. *Lưu ý (nếu chọn External)*: Tại bước **Test users**, anh bắt buộc phải nhấn **+ Add Users** và điền chính xác địa chỉ Gmail cá nhân của anh để có quyền đăng nhập thử nghiệm.

### Bước 2.3: Tạo thông tin xác thực OAuth Client
1. Vào menu bên trái -> Chọn **APIs & Services** -> **Credentials**.
2. Nhấp vào nút **+ Create Credentials** ở cạnh trên -> Chọn **OAuth client ID**.
3. Chọn **Application type**: **Desktop app** (Ứng dụng máy tính để bàn).
4. Điền tên: `Workspace MCP Client` -> Nhấn **Create**.
5. Màn hình sẽ hiện hộp thoại chứa **Client ID** và **Client Secret**. Hãy copy hai giá trị này.

### Bước 2.4: Kích hoạt các API dịch vụ Google Workspace
Tại ô tìm kiếm ở đầu trang Google Cloud Console, tìm kiếm và nhấn **Enable** cho từng API sau:
* **Gmail API**
* **Google Drive API**
* **Google Calendar API**
* **Google Tasks API**
* **Google Docs API**
* **Google Sheets API**

### Bước 2.5: Điền thông tin vào mcp_config.json
Mở tệp [mcp_config.json](file:///C:/Users/vu.hoang/.gemini/antigravity/mcp_config.json) và thay thế phần giá trị placeholder bằng thông tin vừa lấy:
```json
"GOOGLE_OAUTH_CLIENT_ID": "123456789-abcdef.apps.googleusercontent.com",
"GOOGLE_OAUTH_CLIENT_SECRET": "GOCSPX-xxxxxxxxxxxxx"
```

---

## 3. KHỞI CHẠY & KIỂM TRA (SMOKE TEST)
Sau khi anh điền thông tin, lần đầu tiên Antigravity hoặc Claude Code gọi công cụ liên quan đến Workspace, một tab trình duyệt sẽ tự động mở ra yêu cầu anh đăng nhập tài khoản Google và nhấn **Allow (Cho phép)** cấp quyền truy cập. 

Sau khi xác thực thành công, anh có thể yêu cầu Antigravity thực hiện các lệnh như:
* *"Liệt kê 5 email chưa đọc gần nhất"*
* *"Tìm các file tài liệu có tên 'Báo cáo UAT' trong Google Drive của tao"*
* *"Thêm lịch họp vào Google Calendar lúc 2h chiều mai"*
