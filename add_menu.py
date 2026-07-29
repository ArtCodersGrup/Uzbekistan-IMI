import glob

files = glob.glob('*.html')
for file in files:
    if file == 'admin.html':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = '<a href="teachers.html">O\'qituvchilar</a>'
    replacement = '<a href="teachers.html">O\'qituvchilar</a>\n        <a href="sorovnomalar.html">So\'rovnomalar</a>'
    
    # Check if not already added
    if 'sorovnomalar.html' not in content:
        # replace in desktop nav
        content = content.replace(target, replacement)
        
        # for mobile nav it might have different spacing (target2)
        target2 = '<a href="teachers.html">O\'qituvchilar</a>'
        # actually we replaced all occurrences. We can just double check.
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Menu patched on all public pages.")
