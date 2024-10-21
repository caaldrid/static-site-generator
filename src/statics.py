import os
import shutil


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
