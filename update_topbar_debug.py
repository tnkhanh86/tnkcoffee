import os

base_dir = r"d:/testAntigravity/TKWeb_Python/WebCoffee/pages/templates/pages"
files = ["index.html", "about.html", "menu.html", "news.html", "contact.html"]

def update_topbar():
    print("Starting update...")
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filename}")
            continue
        
        print(f"Processing {filename}...")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        # Replace Email
        if "<span>info@example.com</span>" in content:
            content = content.replace("<span>info@example.com</span>", "<span>tnk@gmail.com</span>")
            print(f"  Updated email in {filename}")
            modified = True
        else:
            print(f"  Email placeholder not found in {filename}")

        # Replace Phone
        if "<span>+012 345 6789</span>" in content:
            content = content.replace("<span>+012 345 6789</span>", "<span>0933.xxx.xxx</span>")
            print(f"  Updated phone in {filename}")
            modified = True
        else:
            print(f"  Phone placeholder not found in {filename}")
        
        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Saved {filename}")

if __name__ == "__main__":
    update_topbar()
