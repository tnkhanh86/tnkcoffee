import os
import re

file_paths = [
    'pages/templates/pages/index.html',
    'pages/templates/pages/menu.html',
]

for path in file_paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to match {{ followed by any whitespace (including newlines) then cart|length then whitespace then }}
        pattern = re.compile(r'\{\{\s*cart\|length\s*\}\}')
        
        # Replace with single line compact version
        new_content = pattern.sub('{{ cart|length }}', content)
        
        if content != new_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {path}")
        else:
            print(f"No changes for {path} (Pattern not found or already correct)")
    else:
        print(f"File not found: {path}")
