python ..\Labelme2YOLO\labelme2yolo.py^
 --labels_dir "C:\Users\david\Documents\source\datasets\uvigo_limburg_labelme\labels\train"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo_limburg\labels\train"^
 --multi_video^
 --shift_class_id -1 ^
 --image_width 3840 ^
 --image_height 2160

python ..\Labelme2YOLO\labelme2yolo.py^
 --labels_dir "C:\Users\david\Documents\source\datasets\uvigo_limburg_labelme\labels\val"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo_limburg\labels\val"^
 --multi_video^
 --shift_class_id -1 ^
 --image_width 3840 ^
 --image_height 2160

 python merge_dirs.py^
 --parent_dir "C:\Users\david\Documents\source\datasets\uvigo_limburg_labelme\images\train"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo_limburg\images\train"

  python merge_dirs.py^
 --parent_dir "C:\Users\david\Documents\source\datasets\uvigo_limburg_labelme\images\val"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo_limburg\images\val"