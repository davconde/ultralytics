import os
import argparse
import shutil


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--parent_dir', help='Directory with subfolders',
                        required=False)
    parser.add_argument('--target_dir', help='Destination folder',
                        required=False)
    args = parser.parse_args()

    parent_dir = args.parent_dir
    target_dir = args.target_dir

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    source_dirs = [os.path.join(parent_dir, dir) for dir in os.listdir(parent_dir)\
                   if os.path.isdir(os.path.join(parent_dir, dir))]
    
    for source_dir in source_dirs:
        for file in os.listdir(source_dir):
            src_file = os.path.join(source_dir, file)
            if os.path.isfile(src_file):
                shutil.copyfile(src_file, os.path.join(target_dir, file))
