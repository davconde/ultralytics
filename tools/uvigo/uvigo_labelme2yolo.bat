python ..\Labelme2YOLO\labelme2yolo.py^
 --labels_dir "C:\Users\david\Documents\source\datasets\uvigo_labelme\labels\train"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo\labels\train"^
 --multi_video

python ..\Labelme2YOLO\labelme2yolo.py^
 --labels_dir "C:\Users\david\Documents\source\datasets\uvigo_labelme\labels\val"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo\labels\val"^
 --multi_video

 python merge_dirs.py^
 --parent_dir "C:\Users\david\OneDrive - Universidade de Vigo\Data\toAnnotate\data\train"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo\images\train"

  python merge_dirs.py^
 --parent_dir "C:\Users\david\OneDrive - Universidade de Vigo\Data\toAnnotate\data\test"^
 --target_dir "C:\Users\david\Documents\source\datasets\uvigo\images\val"