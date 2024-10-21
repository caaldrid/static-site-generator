import os

from statics import copy_static_to_public, generate_page


def main():
    copy_static_to_public()

    cwd = os.getcwd()
    index_path = os.path.join(cwd, "content", "index.md")
    template_path = os.path.join(cwd, "template.html")

    generate_page(index_path, template_path, os.path.join(cwd, "public", "index.html"))


if __name__ == "__main__":
    main()
