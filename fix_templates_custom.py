import os

file_paths = [
    'pages/templates/pages/index.html',
    'pages/templates/pages/about.html',
    'pages/templates/pages/news.html',
    'pages/templates/pages/contact.html',
]

for path in file_paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace split tag with joined tag (handling various indentation/newline)
        # We target the specific split seen in verification
        new_content = content.replace('{{\n                        cart|length }}', '{{ cart|length }}')
        new_content = new_content.replace('{{\r\n                        cart|length }}', '{{ cart|length }}')
        
        # Also clean up any other variations if my grep was slightly off, e.g. different spaces
        # Using a regex-like approach via simple split/join if needed, but strict string replacement is safer if pattern matches
        
        if content != new_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {path}")
        else:
            print(f"No changes for {path} (Pattern not found or already fixed)")
    else:
        print(f"File not found: {path}")
