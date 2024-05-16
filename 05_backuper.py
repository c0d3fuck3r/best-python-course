# Explain os module

import os
import shutil


if __name__ == "__main__":

    src_dir = os.getcwd()
    dst_dir = os.path.join(src_dir, "backup")

    # for file in os.listdir(src_dir):
    #     print(file)

    # check if backup dir exists. create if not
    if not os.path.exists(dst_dir):
        print(f"Backup dir {dst_dir} does not exist.")
        print("Creating...")
        os.mkdir(dst_dir)

    total_bytes = 0

    # copy each file(not dirs) to backup dir
    for file in os.listdir(src_dir):
        if not os.path.isdir(file):
            total_bytes += os.path.getsize(file)
            shutil.copy(file, dst_dir)

    print("Backup completed.")
    total_mb = round((total_bytes / 1024 / 1024), 2)
    # total_mb = "%.2f" % (total_bytes / 1024 / 1024)
    print(f"{total_mb} MB copied.")
