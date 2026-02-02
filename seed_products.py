
import os
import django
import re
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebCoffee.settings')
django.setup()

from pages.models import Category, Product

def run():
    # Clear existing data
    Product.objects.all().delete()
    Category.objects.all().delete()
    print("Cleared existing data.")

    # Create Categories
    # We need to map Tab IDs to Categories
    categories = {
        "tab-1": Category.objects.create(name="Cà phê", slug="ca-phe"),
        "tab-2": Category.objects.create(name="Freeze", slug="freeze"),
        "tab-3": Category.objects.create(name="Trà", slug="tra"),
        "tab-4": Category.objects.create(name="Bánh ngọt", slug="banh-ngot")
    }
    print("Categories created.")

    # Read menu.html
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    menu_path = os.path.join(BASE_DIR, 'pages', 'templates', 'pages', 'menu.html')
    
    with open(menu_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    total_added = 0
    
    for tab_id, category in categories.items():
        tab_div = soup.find('div', id=tab_id)
        if not tab_div:
            print(f"Tab {tab_id} not found!")
            continue

        # Find all product items in this tab
        # Structure: .col-lg-6 -> .d-flex -> img, h4(price), h5(name), span.product-description
        items = tab_div.find_all('div', class_='col-lg-6')
        
        for item in items:
            try:
                # Extract Name
                name_tag = item.find('h5')
                name = name_tag.get_text(strip=True) if name_tag else "Unknown"

                # Extract Price
                price_tag = item.find('h4')
                price_str = price_tag.get_text(strip=True) if price_tag else "0"
                # Remove non-numeric characters for price (e.g. 29.000đ -> 29000)
                price = int(re.sub(r'\D', '', price_str))

                # Extract Description
                desc_tag = item.find('span', class_='product-description')
                desc = desc_tag.get_text(strip=True) if desc_tag else ""

                # Extract Image
                img_tag = item.find('img')
                # src is like "{% static 'pages/images/...' %}"
                if img_tag and 'src' in img_tag.attrs:
                    raw_src = img_tag['src']
                    # Parse djangostatic tag using regex
                    # match: {% static 'path' %} or "{% static 'path' %}"
                    match = re.search(r"static\s+['\"]([^'\"]+)['\"]", raw_src)
                    if match:
                        image_url = match.group(1)
                    else:
                        image_url = raw_src # Fallback
                else:
                    image_url = ""

                # Create Product
                Product.objects.create(
                    category=category,
                    name=name,
                    price=price,
                    description=desc,
                    image_url=image_url
                )
                total_added += 1
            except Exception as e:
                print(f"Error parsing item: {e}")

    print(f"Database seeded successfully with {total_added} products!")

if __name__ == '__main__':
    run()
