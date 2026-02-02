import os
import re

base_dir = r"d:/testAntigravity/TKWeb_Python/WebCoffee/pages/templates/pages"
files = ["index.html", "about.html", "menu.html", "news.html", "contact.html"]

def fix_content(content):
    # Remove backslashes before single quotes inside django tags
    # We essentially want to turn \' into ' globally in these files, 
    # but to be safe we can target the specific patterns we created.
    
    # The previous script likely produced: {% static \'...\' %} and {% url \'...\' %}
    
    # Fix static tags
    content = content.replace(r"{% static \'pages/", r"{% static 'pages/")
    content = content.replace(r"\' %}", r"' %}")
    
    # Fix url tags
    content = content.replace(r"{% url \'", r"{% url '")
    
    # Just in case there are others slightly different, let's do a generic replace
    # for expected patterns if the above is too specific.
    # But the above covers the start and end. 
    # Let's also check for internal quotes if any (unlikely for filenames).
    
    return content

for file in files:
    path = os.path.join(base_dir, file)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = fix_content(content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {file}")
    else:
        print(f"File {file} not found")
