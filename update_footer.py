import os

base_dir = r"d:/testAntigravity/TKWeb_Python/WebCoffee/pages/templates/pages"
files = ["index.html", "about.html", "menu.html", "news.html", "contact.html"]

NEW_FOOTER = """    <!-- Footer Start -->
    <div class="container-fluid bg-img text-secondary" style="margin-top: 90px">
        <div class="container">
            <div class="row gx-5">
                <div class="col-lg-4 col-md-6 mb-lg-n5">
                    <div
                        class="d-flex flex-column align-items-center justify-content-center text-center h-100 bg-primary border-inner p-4">
                        <a href="{% url 'home' %}" class="navbar-brand">
                            <h1 class="m-0 text-uppercase text-white"><i
                                    class="fa fa-mug-hot fs-1 text-dark me-3"></i>TNK Coffee</h1>
                        </a>
                        <p class="mt-3">TNK Coffee là thiên đường của những chiếc bánh ngọt ngào. Chúng tôi luôn đặt tâm
                            huyết vào từng sản phẩm để mang lại trải nghiệm tuyệt vời nhất cho khách hàng.</p>
                    </div>
                </div>
                <div class="col-lg-8 col-md-6">
                    <div class="row gx-5">
                        <div class="col-lg-4 col-md-12 pt-5 mb-5">
                            <h4 class="text-primary text-uppercase mb-4">Liên Hệ Chúng Tôi</h4>
                            <div class="d-flex mb-2">
                                <i class="bi bi-geo-alt text-primary me-2"></i>
                                <p class="mb-0">227 Nguyễn Văn Cừ, Chợ Quán, TpHCM</p>
                            </div>
                            <div class="d-flex mb-2">
                                <i class="bi bi-envelope-open text-primary me-2"></i>
                                <p class="mb-0">tnk@gmail.com</p>
                            </div>
                            <div class="d-flex mb-2">
                                <i class="bi bi-telephone text-primary me-2"></i>
                                <p class="mb-0">0933.xxx.xxx</p>
                            </div>
                            <div class="d-flex mt-4">
                                <a class="btn btn-lg btn-primary btn-lg-square border-inner rounded-0 me-2" href="#"><i
                                        class="fab fa-twitter fw-normal"></i></a>
                                <a class="btn btn-lg btn-primary btn-lg-square border-inner rounded-0 me-2" href="#"><i
                                        class="fab fa-facebook-f fw-normal"></i></a>
                                <a class="btn btn-lg btn-primary btn-lg-square border-inner rounded-0 me-2" href="#"><i
                                        class="fab fa-linkedin-in fw-normal"></i></a>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-12 pt-0 pt-lg-5 mb-5">
                            <h4 class="text-primary text-uppercase mb-4">Liên Kết Nhanh</h4>
                            <div class="d-flex flex-column justify-content-start">
                                <a class="text-secondary mb-2" href="{% url 'home' %}"><i
                                        class="bi bi-arrow-right text-primary me-2"></i>Trang Chủ</a>
                                <a class="text-secondary mb-2" href="{% url 'about' %}"><i
                                        class="bi bi-arrow-right text-primary me-2"></i>Giới Thiệu</a>
                                <a class="text-secondary mb-2" href="{% url 'menu' %}"><i
                                        class="bi bi-arrow-right text-primary me-2"></i>Thực Đơn</a>
                                <a class="text-secondary mb-2" href="{% url 'news' %}"><i
                                        class="bi bi-arrow-right text-primary me-2"></i>Tin Tức</a>
                                <a class="text-secondary" href="{% url 'contact' %}"><i
                                        class="bi bi-arrow-right text-primary me-2"></i>Liên Hệ</a>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-12 pt-0 pt-lg-5 mb-5">
                            <h4 class="text-primary text-uppercase mb-4">Bản Tin</h4>
                            <p>Đăng ký nhận tin để cập nhật những ưu đãi mới nhất từ chúng tôi.</p>
                            <form action="">
                                <div class="input-group">
                                    <input type="text" class="form-control border-white p-3" placeholder="Email của bạn">
                                    <button class="btn btn-primary">Đăng Ký</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container-fluid text-secondary py-4" style="background: #111111;">
        <div class="container text-center">
            <p class="mb-0">&copy; <a class="text-white border-bottom" href="#">TNK Coffee</a>. Bảo lưu mọi quyền.
                
                <!--/*** This template is free as long as you keep the footer author’s credit link/attribution link/backlink. If you'd like to use the template without the footer author’s credit link/attribution link/backlink, you can purchase the Credit Removal License from "https://htmlcodex.com/credit-removal". Thank you for your support. ***/-->
                Thiết kế bởi <a class="text-white border-bottom" href="https://htmlcodex.com">HTML Codex</a>
            </p>
        </div>
    </div>
    <!-- Footer End -->"""

def update_footer():
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filename}")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Find start and end of Footer
        start_marker = "<!-- Footer Start -->"
        end_marker = "<!-- Footer End -->"
        
        start_idx = content.find(start_marker)
        if start_idx == -1:
            print(f"Footer start marker not found in {filename}")
            continue
            
        # Find the end of the footer block. Since "Footer End" is part of the replacement, 
        # we need to find where the current footer ends.
        # Based on index.html view, there is "<!-- Footer End -->" at the end.
        
        # However, be careful: NEW_FOOTER includes "<!-- Footer Start -->" and "<!-- Footer End -->"
        # So we should replace from start_marker to end_marker + len(end_marker)
        
        end_idx = content.find(end_marker, start_idx)
        if end_idx == -1:
            print(f"Footer end marker not found in {filename}")
            continue
            
        end_idx += len(end_marker)
        
        new_content = content[:start_idx] + NEW_FOOTER + content[end_idx:]
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated footer in {filename}")

if __name__ == "__main__":
    update_footer()
