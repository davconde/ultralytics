python ..\Labelme2YOLO\labelme2yolo.py^
 --labels_dir "C:\Users\david\Documents\source\datasets\uvigo_cones_labelme\labels\train"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo_cones\labels\train"^
 --multi_video^
 --shift_class_id -1

python ..\Labelme2YOLO\labelme2yolo.py^
 --labels_dir "C:\Users\david\Documents\source\datasets\uvigo_cones_labelme\labels\val"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo_cones\labels\val"^
 --multi_video^
 --shift_class_id -1

 python merge_dirs.py^
 --parent_dir "C:\Users\david\Documents\source\datasets\uvigo_cones_labelme\images\train"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo_cones\images\train"

  python merge_dirs.py^
 --parent_dir "C:\Users\david\Documents\source\datasets\uvigo_cones_labelme\images\val"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo_cones\images\val"