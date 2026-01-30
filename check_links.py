
import requests

links = [
    "https://nld.com.vn/gia-ca-phe-viet-nam-tang-manh-theo-da-the-gioi-196251224151322744.htm",
    "https://nld.com.vn/gia-ca-phe-hom-nay-26-1-trung-quoc-bat-ngo-tang-manh-nhap-khau-196260126075654841.htm",
    "https://nld.com.vn/gia-ca-phe-hom-nay-25-1-gia-tang-3-con-so-196260125075607757.htm"
]

def check_links(urls):
    for url in urls:
        try:
            response = requests.head(url, timeout=5, allow_redirects=True)
            if response.status_code == 200:
                print(f"[OK] {url}")
            else:
                print(f"[BROKEN - {response.status_code}] {url}")
        except Exception as e:
            print(f"[ERROR - {str(e)}] {url}")

if __name__ == "__main__":
    check_links(links)
