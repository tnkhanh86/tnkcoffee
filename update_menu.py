
import csv
import os
import re

# Paths
BASE_DIR = r"d:\testAntigravity\TKWeb_Python"
CATEGORY_CSV = os.path.join(BASE_DIR, "app_shop_category.csv")
PRODUCT_CSV = os.path.join(BASE_DIR, "app_shop_product.csv")
TEMPLATE_DIR = os.path.join(BASE_DIR, "cake-shop-website-template")
MENU_HTML_PATH = os.path.join(TEMPLATE_DIR, "menu.html")

def read_csv(filepath):
    data = []
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def generate_tabs_html(categories):
    html = '<ul class="nav nav-pills d-inline-flex justify-content-center bg-dark text-uppercase border-inner p-4 mb-5">\n'
    for index, cat in enumerate(categories):
        active_class = "active" if index == 0 else ""
        html += f'                    <li class="nav-item">\n'
        html += f'                        <a class="nav-link text-white {active_class}" data-bs-toggle="pill" href="#tab-{cat["id"]}">{cat["name"]}</a>\n'
        html += f'                    </li>\n'
    html += '                </ul>'
    return html

def generate_products_html(categories, products):
    html = '<div class="tab-content">\n'
    for index, cat in enumerate(categories):
        cat_id = cat['id']
        active_class = "active" if index == 0 else ""
        
        # Filter products for this category
        cat_products = [p for p in products if p['category_id'] == cat_id]
        
        html += f'                    <div id="tab-{cat_id}" class="tab-pane fade show p-0 {active_class}">\n'
        html += '                        <div class="row g-3">\n'
        
        for prod in cat_products:
            # Handle image path - CSV has relative path, we might need to adjust or keep it
            # Assuming CSV paths like "images/products/..." are correct relative to menu.html parent or need adjustment
            # menu.html is in cake-shop-website-template. 
            # If images are in d:\testAntigravity\TKWeb_Python\images, and menu.html is in d:\testAntigravity\TKWeb_Python\cake-shop-website-template\menu.html
            # then path to images should be ../images/products/...
            # Let's adjust the path.
            
            # Assuming images are in cake-shop-website-template/images/products/...
            # and menu.html is in cake-shop-website-template/menu.html
            # The CSV path is like "images/products/..."
            # So we just need to use it as is, or ensuring forward slashes.
            
            img_path = prod['image'].replace('\\', '/')
            # No need to add ../ if the images folder is in the same directory as menu.html's root


            name = prod['name']
            price = f"{int(prod['price']):,}".replace(",", ".") + "đ" # Basic formatting
            desc = prod['description']
            if not desc:
                desc = "Chưa có thông tin"
            
            html += '                            <div class="col-lg-6">\n'
            html += '                                <div class="d-flex h-100">\n'
            html += '                                    <div class="flex-shrink-0">\n'
            html += f'                                        <img class="img-fluid" src="{img_path}" alt="" style="width: 150px; height: 85px; object-fit: cover;">\n'
            html += f'                                        <h4 class="bg-dark text-primary p-2 m-0">{price}</h4>\n'
            html += '                                    </div>\n'
            html += '                                    <div class="d-flex flex-column justify-content-center text-start bg-secondary border-inner px-4 product-info-box">\n'
            html += f'                                        <h5 class="text-uppercase">{name}</h5>\n'
            html += f'                                        <span class="product-description">{desc}</span>\n'
            html += '                                    </div>\n'
            html += '                                </div>\n'
            html += '                            </div>\n'
            
        html += '                        </div>\n'
        html += '                    </div>\n'
        
    html += '                </div>'
    return html

def update_menu_html():
    print("Reading data...")
    categories = read_csv(CATEGORY_CSV)
    products = read_csv(PRODUCT_CSV)
    
    # Sort categories by ID just in case
    categories.sort(key=lambda x: int(x['id']))
    
    print("Generating HTML...")
    new_tabs_html = generate_tabs_html(categories)
    new_products_html = generate_products_html(categories, products)
    
    print(f"Reading {MENU_HTML_PATH}...")
    with open(MENU_HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Tabs
    # Regex to find the <ul> with class "nav nav-pills..."
    # We look for the start tag and the closing </ul>
    
    # NOTE: The pattern needs to be robust. 
    # Existing tabs: <ul class="nav nav-pills d-inline-flex justify-content-center bg-dark text-uppercase border-inner p-4 mb-5"> ... </ul>
    
    tabs_pattern = re.compile(r'<ul class="nav nav-pills.*?</ul>', re.DOTALL)
    
    if not tabs_pattern.search(content):
        print("Error: Could not find tabs section in HTML")
        return

    content = tabs_pattern.sub(new_tabs_html, content)
    
    # Replace Content
    # Existing content: <div class="tab-content"> ... </div>
    # This is a bit riskier if there are nested divs with the same closing logic, but the tab-content usually wraps everything.
    # We can match <div class="tab-content"> until the last matching </div> for it.
    
    # Simpler regex might be: <div class="tab-content">.*?</div> inside the specific parent container? 
    # Or just replace the whole block we identified in the template.
    
    # Let's try to find <div class="tab-content"> and the matching closing div. 
    # Since regex is greedy or lazy, and nested divs exist, regex is hard for nested structures.
    # However, in this template, the structure is indentation based or specific.
    # Let's assume standard formatting or use a string replace if possible.
    
    # The template has:
    # <div class="tab-class text-center">
    #     <ul ...> ... </ul>
    #     <div class="tab-content"> ... </div>
    # </div>
    
    # We can reconstruct the whole .tab-class div content if we want, but let's try regex for tab-content since it's distinct.
    
    content_pattern = re.compile(r'<div class="tab-content">.*?</div>\s*</div>\s*</div>', re.DOTALL) 
    # ^ This is risky because we don't know how many closing divs are matched.
    
    # Alternative: Use simple string identifiers if they are unique enough.
    start_marker = '<div class="tab-content">'
    # We need to find the close of this div. 
    # Given the previous reading of file:
    # Line 128: <div class="tab-content">
    # Line 357:                 </div>
    # Line 358:             </div> (closes tab-class)
    
    # Let's use string finding and counting braces if needed, but for now let's try a regex that expects the specific structure shown in `view_file`.
    
    content_match = re.search(r'(<div class="tab-content">.*?)(\s*</div>\s*</div>\s*</div>)', content, re.DOTALL)
    # The file ends with 3 closing divs: tab-content, tab-class, container?
    # No:
    # 357: </div> (tab-content)
    # 358: </div> (tab-class)
    # 359: </div> (container)
    # 360: </div> (row/container-fluid)
    
    # Let's construct the replacement strictly.
    # We can simply replace the whole `<div class="tab-class text-center">` block if we want, but that includes the tabs we just replaced?
    # Actually, if we replaced the tabs effectively, we have new tabs but old content.
    
    # Let's try to locate the start and end of `div class="tab-content"` manually.
    
    start_idx = content.find('<div class="tab-content">')
    if start_idx == -1:
         print("Error: Could not find tab-content start")
         return
         
    # Find the end. Since `tab-content` contains `tab-pane` divs, we can't just search for first </div>.
    # But looking at the file, the indentation is helpful or we just replace everything between start_idx and the known footer of that section.
    
    # In `menu.html`, after tab-content ends (line 357), we have:
    # 358:             </div>
    # 359:         </div>
    # 360:     </div>
    # 361:     <!-- Products End -->
    
    end_marker = '<!-- Products End -->'
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
        print("Error: Could not find Products End marker")
        return
        
    # Now we act more locally. between 'start_idx' and 'end_idx', we want to remove everything except the closing divs that belong to parents.
    # The 'tab-content' div is closed before the parents.
    # Let's look backwards from 'end_idx' to find the closing of 'tab-content'? No, that's messy.
    
    # Let's trust that `tab-content` is the last big block before the closing divs of the section.
    # The structure:
    # <div class="tab-class ...">
    #    <ul>...</ul>
    #    <div class="tab-content">
    #       ...
    #    </div>
    # </div>
    
    # If we replace regex `r'<div class="tab-content">.*?(?=</div>\s*</div>\s*</div>)'` it might work?
    # Actually, simpler: We replaced the `ul`. Now the string has the new `ul`.
    # Let's find `<div class="tab-content">` again (position might have changed).
    
    # Let's just create the WHOLE `tab-class` div content.
    full_section_html = f'<div class="tab-class text-center">\n{new_tabs_html}\n{new_products_html}\n            </div>'
    
    # Now replace the entire `<div class="tab-class text-center">...</div>` block.
    # We need to find where it starts and ends.
    block_start = '<div class="tab-class text-center">'
    
    # To find the end, let's use the fact that it is inside `<div class="container-fluid about py-5"> <div class="container"> ... `
    # And followed by `</div> </div> </div> <!-- Products End -->`
    
    # Let's try regex for the whole block.
    full_block_pattern = re.compile(r'<div class="tab-class text-center">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
    # The closing divs logic is fragile.
    
    # BETTER APPROACH:
    # We know the content between `<!-- Products Start -->` and `<!-- Products End -->`.
    # Let's parse that region.
    
    products_start_marker = '<!-- Products Start -->'
    products_end_marker = '<!-- Products End -->'
    
    p_start = content.find(products_start_marker)
    p_end = content.find(products_end_marker)
    
    if p_start != -1 and p_end != -1:
        section_content = content[p_start:p_end]
        
        # We only want to replace the `tab-class` part inside this section.
        # But maybe we can reconstruct the surrounding containers if we are careful, 
        # OR just find the `tab-class` div inside this substring.
        
        # Let's try to match the `tab-class` div inside the whole file content, relying on its class name.
        # It opens at line 116.
        # It closes at line 358.
        
        # Regex to capture balanced divs is impossible, but we can assume valid HTML structure and "last div before Products End minus 2"?
        
        # Let's try this:
        # Find start of tab-class.
        tc_start = content.find('<div class="tab-class text-center">')
        
        # Find end of tab-class. It is followed by </div>\n</div>\n</div>\n<!-- Products End -->
        # So counting back from Products End is safer.
        # The file has:
        # ...
        #             </div> (End of tab-class)
        #         </div> (End of container)
        #     </div> (End of container-fluid)
        #     <!-- Products End -->
        
        # So the `tab-class` div content ends just before the last 2 `</div>`s before the marker.
        
        substring_before_end = content[:p_end]
        # Find the last `</div>`
        last_div = substring_before_end.rfind('</div>')
        # Find second last
        second_last = substring_before_end.rfind('</div>', 0, last_div)
        # Find third last (which is the closing of tab-class)
        third_last = substring_before_end.rfind('</div>', 0, second_last)
        
        tc_end = third_last + 6 # include </div>
        
        if tc_start != -1 and tc_end > tc_start:
            prefix = content[:tc_start]
            suffix = content[tc_end:]
            content = prefix + full_section_html + suffix
            
            with open(MENU_HTML_PATH, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully updated menu.html!")
        else:
            print("Error: Could not calculate tab-class boundaries.")

if __name__ == "__main__":
    update_menu_html()
