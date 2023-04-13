import os
import argparse


def convert_to_yolo(kitti_path, yolo_path, size):
    # open KITTI annotation file
    with open(kitti_path, 'r') as f:
        annotations = f.readlines()

    # convert annotations to YOLO format
    yolo_annotations = []
    for ann in annotations:
        ann = ann.split()
        obj_class = int(ann[0])
        dw = 1. / size[0]
        dh = 1. / size[1]
        x_min = float(ann[4])
        y_min = float(ann[5])
        x_max = float(ann[6])
        y_max = float(ann[7])

        # convert to YOLO format
        x_center = (x_min + x_max) / 2.0
        y_center = (y_min + y_max) / 2.0
        width = x_max - x_min
        height = y_max - y_min
        x_center *= dw
        y_center *= dh
        width *= dw
        height *= dh

        # add to list of YOLO annotations
        yolo_annotations.append(f"{obj_class} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

    # write YOLO annotations to file
    with open(yolo_path, 'w') as f:
        f.writelines(yolo_annotations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--labels_dir', help='Directory with KITTI labels',
                        required=True)
    parser.add_argument('--target_dir', help='Directory for target YOLO labels',
                        required=False, default=None)
    parser.add_argument('--img_width', type=int, help='Image width',
                        required=True)
    parser.add_argument('--img_height', type=int, help='Image height',
                        required=True)
    args = parser.parse_args()
    labels_dir = args.labels_dir
    target_dir = args.target_dir
    img_width = args.img_width
    img_height = args.img_height
    if target_dir is None:
        target_dir = os.path.join(labels_dir, 'YOLO')

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for file in os.listdir(labels_dir):
        src_file = os.path.join(labels_dir, file)
        if os.path.isfile(src_file):
            convert_to_yolo(src_file, os.path.join(target_dir, file), (img_width, img_height))
