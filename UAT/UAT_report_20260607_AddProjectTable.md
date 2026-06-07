# 🧪 BÁO CÁO KIỂM THỬ NGHIỆM THU NGƯỜI DÙNG (UAT REPORT)
**Tên file**: `UAT_report_20260607_AddProjectTable.md`  
**Ngày thực hiện**: 07/06/2026  
**Dự án**: Research (Danh mục dự án AI mã nguồn mở - Phiên bản Bảng chi tiết & Google Workspace MCP)  
**Tác giả**: Antigravity Agent  

---

## 1. THÔNG TIN CHUNG (OVERVIEW)
Báo cáo này ghi nhận kết quả kiểm thử nghiệm thu thực tế (`UAT` - User Acceptance Testing) cho việc tích hợp **Bảng tổng hợp chi tiết** và dự án thứ 14 **Google Workspace MCP** tìm thấy từ lịch sử chat của Jun Vuhoang.
* **Môi trường**: Vercel Production
* **Đường dẫn Live URL**: [https://vietnam-open-source-ai-projects.vercel.app](https://vietnam-open-source-ai-projects.vercel.app)
* **Nhánh kiểm thử**: `master`

---

## 2. DỰ ÁN AI MỚI TRÍCH XUẤT TỪ CHAT (GOOGLE WORKSPACE MCP)
* **Tên Repo**: `taylorwilsdon/google_workspace_mcp`
* **Đường dẫn**: [https://github.com/taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)
* **Mục đích**: MCP Server kết nối các AI Agent (như Claude, Codex, Antigravity) trực tiếp với các dịch vụ Google Workspace (Gmail, Drive, Docs, Sheets, Calendar, Forms, Tasks...).
* **Cách cài đặt & khởi chạy nhanh**:
  * Chạy trực tiếp qua `uvx` (Khuyên dùng):
    ```bash
    uvx workspace-mcp --tool-tier core
    ```
  * Chạy ở chế độ không cần cấu hình Google Client (Secretless):
    ```bash
    npx -y @taylorwilsdon/workspace-mcp --secretless
    ```
  * Cấu hình OAuth Client ID dạng **Desktop application** trên Google Cloud Console và thiết lập các biến môi trường:
    ```bash
    export GOOGLE_OAUTH_CLIENT_ID="your-client-id.apps.googleusercontent.com"
    export GOOGLE_OAUTH_CLIENT_SECRET="your-client-secret"
    ```
  * Chạy server ở chế độ HTTP streamable:
    ```bash
    uvx workspace-mcp --transport streamable-http
    ```
  * Đăng ký server vào Claude Code:
    ```bash
    claude mcp add --transport http workspacemcp http://localhost:8000/mcp
    ```

---

## 3. KẾT QUẢ KIỂM THỬ CHI TIẾT (TEST CASES VERIFICATION)

### Test Case 1: Hiển thị song song cả Cards và Table View
* **Mô tả**: Truy cập trang web và xác nhận phần Cards hiển thị phía trên, phần Bảng tổng hợp hiển thị trực tiếp ngay bên dưới.
* **Trạng thái**: `PASS - normal path` (Vượt qua - luồng chính chạy sạch).
* **Kết quả thực tế (`VERIFIED`)**: Giao diện hiển thị cả hai phần nối tiếp nhau. Không cần nhấn nút toggle ẩn/hiện, giúp xem đối chiếu dễ dàng.
* **Bằng chứng ghi nhận**: WebP video ghi lại hành trình kiểm thử UAT: `C:\Users\vu.hoang\.gemini\antigravity\brain\27381419-c0f8-4ed1-80a1-6d6f2768f882\verify_table_and_mcp_1780806935101.webp`

### Test Case 2: Kiểm tra các cột trong Bảng chi tiết
* **Mô tả**: Kiểm tra xem bảng có đúng 5 cột theo yêu cầu: STT, Tên Repo, Link GitHub, Mục đích, Các ghi chú khác.
* **Trạng thái**: `PASS - normal path` (Vượt qua - luồng chính chạy sạch).
* **Kết quả thực tế (`VERIFIED`)**: Bảng hiển thị chính xác 5 cột được định dạng CSS tối ưu, dễ đọc.
  * Cột 1: STT (Đánh số từ 1 đến 14)
  * Cột 2: Tên Repo / Tác giả
  * Cột 3: Link GitHub (Thẻ liên kết trỏ thẳng sang repository tương ứng)
  * Cột 4: Mục đích (Gồm mô tả khái quát và danh sách gạch đầu dòng "Tình huống áp dụng")
  * Cột 5: Các ghi chú khác (Các lưu ý bảo mật, cấu hình phần cứng nổi bật màu hồng)

### Test Case 3: Kiểm tra sự tồn tại của Google Workspace MCP
* **Mô tả**: Xác nhận dự án `google_workspace_mcp` hiển thị ở cả phần Card và Table ở vị trí số 8.
* **Trạng thái**: `PASS - normal path` (Vượt qua - luồng chính chạy sạch).
* **Kết quả thực tế (`VERIFIED`)**: Dự án được thêm vào danh sách và kết xuất chính xác thông tin mô tả, tình huống áp dụng và ghi chú sử dụng `uvx` / `--secretless`.

### Test Case 4: Lọc dữ liệu đồng bộ
* **Mô tả**: Gõ từ khóa tìm kiếm (ví dụ: "workspace") và kiểm tra cả Card và Table có cùng lọc dữ liệu đồng thời không.
* **Trạng thái**: `PASS - normal path` (Vượt qua - luồng chính chạy sạch).
* **Kết quả thực tế (`VERIFIED`)**: Kết quả tìm kiếm lọc tức thì cả 2 vùng hiển thị. Nhãn đếm dự án cập nhật đúng số lượng.

---

## 4. THỐNG KÊ TRẠNG THÁI GIT & DEPLOYMENT
* **Files safe to stage & committed**:
  * `index.html` (Cập nhật giao diện tích hợp)
  * `Implementation Plan/implementation_plan_20260607_AddProjectTable.md` (Kế hoạch triển khai bảng)
* **Trạng thái đồng bộ**: Master branch và Live URL đã đồng bộ và hoạt động ổn định.
