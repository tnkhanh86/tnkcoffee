
import os

BASE_DIR = r"d:\testAntigravity\TKWeb_Python"
TEMPLATE_DIR = os.path.join(BASE_DIR, "cake-shop-website-template")
MENU_HTML_PATH = os.path.join(TEMPLATE_DIR, "menu.html")

TRANSLATIONS = {
    # Branding
    "CakeZone": "TNK Coffee",
    "Highlands Coffee": "TNK Coffee",
    "Highlands": "TNK Coffee",
    "Cake Shop": "Coffee Shop",
    ">Super Crispy<": ">Đậm Đà<",
    ">Siêu Giòn<": ">Hương Vị Việt<",
    # "Thương Hiệu Cà Phê Việt" is good for TNK too, or we can change it. Let's keep it generic or "TNK Coffee".
    # But wait, previous run changed "The Best Cake In London" -> "Thương Hiệu Cà Phê Việt".
    # So now the file has "Thương Hiệu Cà Phê Việt".
    # If I want to change it to something else, I need to map "Thương Hiệu Cà Phê Việt" -> "New Slogan".
    # Uses generic:
    ">The Best Cake In London<": ">Thương Hiệu Cà Phê Việt<", 
    ">Bánh Ngọt Ngon Nhất<": ">Cà Phê Thượng Hạng<",
    ">Chào Mừng Đến CakeZone<": ">Chào Mừng Đến TNK Coffee<",
    ">Chào Mừng Đến Highlands<": ">Chào Mừng Đến TNK Coffee<",
    
    # Terminology Switches
    "Bánh Ngọt": "Cà Phê",
    "Bánh Sinh Nhật": "Cà Phê Phin",
    "Bánh Cưới": "Cà Phê Freeze",
    "Bánh Theo Yêu Cầu": "Trà & Thức Uống Khác",
    "Bánh Giòn Siêu Ngon": "Hương Vị Đậm Đà", # Hero text
    "Chuyên Gia Bánh": "Chuyên Gia Pha Chế",
    "Birthday Cake": "Cà Phê Phin",
    "Wedding Cake": "Cà Phê Freeze",
    "Custom Cake": "Trà",
    
    # Images - Direct HTML replacement
    'src="img/about.jpg"': 'src="images/products/Phin_Sua_Da.jpg"',
    'src="img/cake-1.jpg"': 'src="images/products/HLC_New_logo_5.1_Products__PHIN_DEN_DA.jpg"',
    'src="img/cake-2.jpg"': 'src="images/products/HLC_New_logo_5.1_Products__PHIN_SUADA.jpg"',
    'src="img/cake-3.jpg"': 'src="images/products/HLC_New_logo_5.1_Products__FREEZE_TRA_XANH.jpg"',
    'data-src="https://www.youtube.com/embed/DWRcNpR6Kdc"': 'data-src="https://www.youtube.com/embed/your_coffee_video_id"', 
    
    # Navigation & Header (Preserve or Update)
    ">Home<": ">Trang Chủ<",
    ">About Us<": ">Giới Thiệu<",
    ">Menu & Pricing<": ">Thực Đơn<",
    ">Master Chefs<": ">Đầu Bếp<",
    ">Pages<": ">Trang<",
    ">Contact Us<": ">Liên Hệ<",
    ">Our Services<": ">Dịch Vụ<",
    ">Testimonial<": ">Đánh Giá<",
    ">Call Us<": ">Gọi Ngay<",
    ">Email Us<": ">Email<",
    
    # Content Updates
    "Chúng tôi tự hào mang đến những chiếc bánh ngọt tuyệt hảo nhất, được làm từ nguyên liệu tươi ngon và niềm đam mê bất tận.": "Chúng tôi tự hào mang đến những ly cà phê đậm đà bản sắc Việt, được chọn lọc từ những hạt cà phê tốt nhất trên vùng cao nguyên.",
    "Với hơn 10 năm kinh nghiệm, CakeZone cam kết mỗi chiếc bánh là một tác phẩm nghệ thuật, không chỉ ngon miệng mà còn đẹp mắt. Chúng tôi luôn nỗ lực không ngừng để mang lại niềm vui cho khách hàng qua từng hương vị.": "Với di sản lâu đời, TNK Coffee cam kết mang đến trải nghiệm cà phê đích thực, nơi hội tụ của những tâm hồn yêu cà phê. Chúng tôi không ngừng sáng tạo để phục vụ cộng đồng.",
    "Với di sản lâu đời, Highlands Coffee cam kết mang đến trải nghiệm cà phê đích thực, nơi hội tụ của những tâm hồn yêu cà phê. Chúng tôi không ngừng sáng tạo để phục vụ cộng đồng.": "Với di sản lâu đời, TNK Coffee cam kết mang đến trải nghiệm cà phê đích thực, nơi hội tụ của những tâm hồn yêu cà phê. Chúng tôi không ngừng sáng tạo để phục vụ cộng đồng.",
    "Chúng tôi cam kết sử dụng nguyên liệu sạch, tự nhiên 100% để đảm bảo sức khỏe cho khách hàng.": "100% hạt cà phê được trồng và thu hoạch thủ công tại Việt Nam, mang trọn hương vị của đất trời.",
    "Hương vị ngọt ngào, thiết kế tinh tế, mang lại niềm vui trọn vẹn cho bữa tiệc của bạn.": "Hương vị đậm đà, lôi cuốn, đánh thức mọi giác quan của bạn mỗi ngày.",
    "Chúng tôi cung cấp dịch vụ làm bánh chuyên nghiệp với nhiều mẫu mã đa dạng, đáp ứng mọi nhu cầu của bạn.": "Thực đơn đa dạng từ Phin truyền thống đến Freeze hiện đại, đáp ứng mọi gu thưởng thức.",
    "Đừng bỏ lỡ danh sách các combo bánh ngọt và đồ uống hấp dẫn đang được giảm giá đặc biệt. Hãy đến và thưởng thức ngay hôm nay!": "Đừng bỏ lỡ các combo Cà Phê và Bánh Mì hấp dẫn. Nạp năng lượng cho ngày mới ngay hôm nay!",
    "Bánh ở đây thực sự rất ngon và đẹp. Tôi đã đặt bánh cho tiệc sinh nhật của gia đình và mọi người đều khen ngợi hết lời.": "Cà phê ở đây rất đậm đà, đúng gu người Việt. Không gian quán cũng rất tuyệt vời để làm việc và gặp gỡ bạn bè.",
    "CakeZone là thiên đường của những chiếc bánh ngọt ngào. Chúng tôi luôn đặt tâm huyết vào từng sản phẩm để mang lại trải nghiệm tuyệt vời nhất cho khách hàng.": "TNK Coffee là nơi thuộc về cộng đồng yêu cà phê. Chúng tôi lan tỏa niềm tự hào Đất Việt qua từng ly cà phê.",
    "Highlands Coffee là nơi thuộc về cộng đồng yêu cà phê. Chúng tôi lan tỏa niềm tự hào Đất Việt qua từng ly cà phê.": "TNK Coffee là nơi thuộc về cộng đồng yêu cà phê. Chúng tôi lan tỏa niềm tự hào Đất Việt qua từng ly cà phê.",
    
    # Contact Page Specifics
    ">Contact Info<": ">Thông Tin Liên Hệ<",

    # Navigation Updates (Page Replacements)
    'href="team.html"': 'href="news.html"',
    '>Đầu Bếp<': '>Tin Tức<',
    '>Đội Ngũ<': '>Tin Tức<', # Footer link
    
    # Text Replacements (for index.html etc)
    ">Thành Viên<": ">Tin Tức<",
    ">Đầu Bếp Hàng Đầu<": ">Tin Tức Mới Nhất<",
    
    # Icons (Optional: Change Birthday Cake icon to Mug Hot?)
    # "fa-birthday-cake": "fa-mug-hot", 
    # ^ This might be risky if fa-mug-hot isn't in the loaded fontawesome version, but usually is standard. Let's try.
    "fa-birthday-cake": "fa-mug-hot",
}

def localize_file(filepath):
    print(f"Localizing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for en, vi in TRANSLATIONS.items():
        content = content.replace(en, vi)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done.")

if __name__ == "__main__":
    # Scan for all HTML files in the template directory
    import glob
    html_files = glob.glob(os.path.join(TEMPLATE_DIR, "*.html"))
    
    # Rename team.html to news.html if it hasn't been done (or just ignore team.html if we delete it later)
    # The script just iterates files. We should probably filter out team.html from processing if we are going to delete it, 
    # to avoid errors or useless work, but it doesn't hurt to process it.
    
    print(f"Found {len(html_files)} HTML files to localize.")
    for file_path in html_files:
        if "team.html" in file_path:
             continue # Skip team.html as it will be deleted
        localize_file(file_path)
