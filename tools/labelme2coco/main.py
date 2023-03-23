# Code from https://github.com/fcakyon/labelme2coco
import argparse
from labelme2coco import get_coco_from_labelme_folder, save_json


def convert(args):
    # set labelme training data directory
    labelme_train_folder = args.train
    # set labelme validation data directory
    labelme_val_folder = args.val
    # set path for coco json to be saved
    export_dir = args.export
    # create train coco object
    train_coco = get_coco_from_labelme_folder(
        labelme_train_folder, args=args)
    # export train coco json
    save_json(train_coco.json, export_dir+"train.json")
    # create val coco object
    val_coco = get_coco_from_labelme_folder(
        labelme_val_folder, coco_category_list=train_coco.json_categories, args=args)
    # export val coco json
    save_json(val_coco.json, export_dir+"val.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t','--train', help='Set labelme training data directory',
        required=False, default='labelme/train')
    parser.add_argument(
        '-v','--val', help='Set labelme validation data directory',
        required=False, default='labelme/val')
    parser.add_argument(
        '-e','--export', help='Set path for coco json to be saved',
        required=False, default='coco')
    parser.add_argument(
        '--imageWidth', help='Set image width if not present in label',
        required=False, default=1920)
    parser.add_argument(
        '--imageHeight', help='Set image height if not present in label',
        required=False, default=1080)
    args = parser.parse_args()
    convert(args)
