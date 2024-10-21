import os
import shutil

from markdown_to_html import extract_title, markdown_to_html_node


def copy_static_to_public():
    def copy_items(from_path, to_path):
        items = os.listdir(from_path)

        for item in items:
            item_path = os.path.join(from_path, item)
            if os.path.isfile(item_path):
                shutil.copy(item_path, to_path)
            else:
                new_to_path = os.path.join(to_path, item)
                os.mkdir(new_to_path)
                copy_items(item_path, new_to_path)

    cwd = os.getcwd()

    path_to_static_dir = os.path.join(cwd, "static")
    path_to_public_dir = os.path.join(cwd, "public")

    if os.path.exists(path_to_public_dir):
        shutil.rmtree(path_to_public_dir)

    os.mkdir(path_to_public_dir)

    copy_items(path_to_static_dir, path_to_public_dir)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path)
    template_file = open(template_path)

    markdown = markdown_file.read()
    template = template_file.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    markdown_file.close()
    template_file.close()

    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    index_file = open(dest_path, mode="w")
    index_file.write(html)
