import os
from block_markdown import markdown_to_html_node
from pathlib import Path 

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("there is no heading")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')


    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_dir = os.listdir(dir_path_content)
    for content in content_dir:
        content_path = os.path.join(dir_path_content,content)
        dest_path = os.path.join(dest_dir_path, content)
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, Path(dest_path).with_suffix(".html"),basepath)
        else:
            generate_pages_recursive(content_path, template_path, dest_path,basepath)

