import os

from statics import copy_static_to_public, generate_pages_recursive


def main():
    copy_static_to_public()

    cwd = os.getcwd()

    generate_pages_recursive(
        os.path.join(cwd, "content"),
        os.path.join(cwd, "template.html"),
        os.path.join(cwd, "public"),
    )


if __name__ == "__main__":
    main()
