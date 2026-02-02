# Hướng Dẫn Deploy Django Project lên PythonAnywhere

Tài liệu này hướng dẫn chi tiết từng bước để đưa website Django của bạn lên PythonAnywhere.

> [!NOTE]
> Tôi đã thực hiện các bước chuẩn bị (Bước 1) trực tiếp trên code của bạn. Bạn có thể bắt đầu từ **Bước 2**.

## Bước 1: Chuẩn Bị Project (Đã thực hiện)

Tôi đã tự động thực hiện các thay đổi sau trên code của bạn để tương thích với PythonAnywhere:
1.  **Tạo `requirements.txt`**: File liệt kê các thư viện cần thiết.
    *Lưu ý: File này hiện chứa khá nhiều thư viện do môi trường của bạn cài nhiều thứ. Nếu khi cài đặt trên PythonAnywhere gặp lỗi "Out of disk space" hoặc quá lâu, bạn có thể chỉ cần cài Django và các thư viện thực sự dùng.*
2.  **Cập nhật `settings.py`**:
    - Thêm `STATIC_ROOT` để quản lý file tĩnh.
    - Cập nhật `ALLOWED_HOSTS = ['*']` để website chạy được trên domain của PythonAnywhere.
    - *Lưu ý*: `DEBUG` vẫn đang là `True`. Khi chạy thật ổn định, bạn nên đổi thành `False`.

---

## Bước 2: Đưa Code lên PythonAnywhere

Cách tốt nhất là sử dụng **GitHub**. Nếu bạn chưa dùng GitHub, bạn có thể upload file ZIP, nhưng GitHub sẽ tiện hơn cho việc cập nhật sau này.

### Cách 1: Sử dụng GitHub (Khuyên dùng)
1.  Tạo tài khoản GitHub và tạo một repository mới (Public hoặc Private).
2.  Mở terminal trên máy tính của bạn (tại thư mục dự án), chạy các lệnh sau để đẩy code lên:
    ```bash
    git init
    git add .
    git commit -m "Initial commit for deployment"
    git branch -M main
    git remote add origin https://github.com/USERNAME/REPO_NAME.git
    git push -u origin main
    ```
    *(Thay `USERNAME` và `REPO_NAME` bằng thông tin của bạn)*

### Cách 2: Upload file ZIP
1.  Nén toàn bộ thư mục `tnkcoffee` thành file `.zip`.
2.  Đăng nhập vào PythonAnywhere -> Tab **Files**.
3.  Upload file zip và dùng **Bash Console** để giải nén (`unzip file.zip`).

---

## Bước 3: Cài Đặt Môi Trường Trên PythonAnywhere

1.  Đăng nhập PythonAnywhere, vào **Dashboard** -> mở **Bash Console**.
2.  Clone code từ GitHub (nếu dùng Cách 1):
    ```bash
    git clone https://github.com/USERNAME/REPO_NAME.git mysite
    ```
    *(Thay link repo của bạn. `mysite` là tên thư mục sẽ tạo)*
3.  Tạo môi trường ảo (virtual environment):
    ```bash
    cd mysite
    mkvirtualenv --python=/usr/bin/python3.10 myvenv
    ```
    *(Lệnh `mkvirtualenv` giúp quản lý môi trường ảo tốt trên PA)*
4.  Cài đặt các thư viện:
    ```bash
    pip install -r requirements.txt
    ```
    *Nếu bị lỗi lâu quá, hãy thử cài thủ công: `pip install django pillow` (và các gói cần thiết khác).*

---

## Bước 4: Cấu Hình Web App

1.  Vào Tab **Web** trên PythonAnywhere -> Chọn **Add a new web app**.
2.  Chọn **Next** -> **Manual configuration** (QUAN TRỌNG: Chọn Manual, không chọn Django auto-config để kiểm soát tốt hơn) -> Chọn **Python 3.10**.
3.  Sau khi tạo xong, tại trang cấu hình Web App:

    ### Cấu hình Virtualenv
    - Tìm mục **Virtualenv**, nhập đường dẫn:
      `/home/USERNAME/.virtualenvs/myvenv`
      *(Thay `USERNAME` bằng tên tài khoản PA của bạn. Dấu check xanh sẽ hiện ra nếu đúng)*

    ### Cấu hình Code
    - **Source code**: Nhập đường dẫn tới thư mục chứa file `manage.py`. 
      - Nếu bạn clone vào `mysite`: `/home/USERNAME/mysite`
    - **Working directory**: Nhập giống Source code (ví dụ `/home/USERNAME/mysite`).

    ### Cấu hình WSGI
    - Nhấp vào link file WSGI configuration (ví dụ: `/var/www/username_pythonanywhere_com_wsgi.py`).
    - Xóa hết nội dung cũ và thay bằng:
      ```python
      import os
      import sys

      # Đường dẫn tới thư mục project của bạn (chứa manage.py)
      path = '/home/USERNAME/mysite'
      if path not in sys.path:
          sys.path.append(path)

      # Trỏ tới file settings của bạn (Thư mục con chứa settings.py)
      os.environ['DJANGO_SETTINGS_MODULE'] = 'WebCoffee.settings'

      from django.core.wsgi import get_wsgi_application
      application = get_wsgi_application()
      ```
      *Lưu ý thay `USERNAME` và đảm bảo `WebCoffee.settings` là đúng (nếu folder settings của bạn tên khác thì sửa lại).*
    - **Lưu lại** (Save).

    ### Cấu hình Static Files (Quan trọng để hiện CSS/Ảnh)
    - Tìm mục **Static files**.
    - Thêm dòng mới:
        - **URL**: `/static/`
        - **Directory**: `/home/USERNAME/mysite/static` 
        *(Lưu ý: Folder `static` này sẽ được tạo ở Bước 5 khi chạy lệnh collectstatic)*

---

## Bước 5: Hoàn Tất

1.  Mở lại **Bash Console**, chạy các lệnh cuối cùng:
    ```bash
    # Vào thư mục dự án
    cd ~/mysite 
    
    # Tạo database & bảng
    python manage.py migrate
    
    # Gom file tĩnh vào thư mục static (để Web tab phục vụ nó)
    python manage.py collectstatic
    
    # Tạo tài khoản admin (nếu cần)
    python manage.py createsuperuser
    ```

2.  Quay lại Tab **Web**, bấm nút **Reload** màu xanh lá cây.
3.  Truy cập vào địa chỉ `username.pythonanywhere.com` để xem kết quả!

> [!TIP]
> Nếu gặp lỗi, hãy kiểm tra **Error Log** trong Tab Web (link nằm ở phía dưới) để biết chi tiết.
