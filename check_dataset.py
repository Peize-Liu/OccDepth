import os

# 定义路径
base_dir = "/home/pliuan/6dof-occ/OccDepth/data/TartanAirOcc/dataset/sequences"
labels_dir = "/home/pliuan/6dof-occ/OccDepth/data/TartanAirOcc/preprocess/labels"

# 获取 base_dir 目录下的所有以数字命名的子文件夹
subfolders = [f for f in os.listdir(base_dir) if f.isdigit() and os.path.isdir(os.path.join(base_dir, f))]

# 记录不匹配的文件夹
mismatch_folders = []

for folder in subfolders:
    folder_num = int(folder)  # 将文件夹名称转换为整数

    image_2_path = os.path.join(base_dir, folder, "image_2")
    voxels_path = os.path.join(base_dir, folder, "voxels")
    label_path = os.path.join(labels_dir, folder)

    # 计算文件数量
    image_2_count = len(os.listdir(image_2_path)) if os.path.exists(image_2_path) else 0
    voxels_count = len(os.listdir(voxels_path)) if os.path.exists(voxels_path) else 0
    label_count = len(os.listdir(label_path)) if os.path.exists(label_path) else 0

    # 输出当前文件夹的文件数量
    if 0 <= folder_num <= 9:
        print(f"Folder {folder}: image_2 = {image_2_count}, voxels = {voxels_count}, labels = {label_count}")
        if not (image_2_count == voxels_count/4 == label_count/2):
            mismatch_folders.append(folder)
    elif 10 <= folder_num <= 14:
        print(f"Folder {folder}: image_2 = {image_2_count}, voxels = {voxels_count}")
        if not image_2_count == voxels_count/4:
            mismatch_folders.append(folder)

# 输出不匹配的文件夹
if mismatch_folders:
    print("\nMismatched folders:")
    for folder in mismatch_folders:
        print(f"- {folder}")
else:
    print("\nAll folders have matching file counts.")