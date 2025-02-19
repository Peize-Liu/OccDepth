import os
import shutil
import argparse
from pathlib import Path

def copy_subfolders(source_dir, target_dir, overwrite=False):
    """
    复制 source_dir 下的所有子文件夹到 target_dir 中，保留相同的子文件夹名称。
    
    :param source_dir: 源目录路径
    :param target_dir: 目标目录路径
    :param overwrite: 是否覆盖目标目录中已存在的同名文件夹
    """
    source = Path(source_dir)
    target = Path(target_dir)
    
    if not source.exists():
        print(f"源目录不存在: {source}")
        return
    
    if not target.exists():
        try:
            target.mkdir(parents=True, exist_ok=True)
            print(f"已创建目标目录: {target}")
        except Exception as e:
            print(f"无法创建目标目录: {target}. 错误: {e}")
            return
    
    # 遍历源目录中的所有子文件夹
    for item in source.iterdir():
        if item.is_dir():
            # print current dir under item
            print(f"正在处理: {item}")
            sequence=item.iterdir()
            sequence_index = item.name
            print(f"sequence_index: {sequence_index}")
            target_path = target / sequence_index / "voxels"
            print(f"target_path: {target_path}") 
            source_voxel_dir = item / "voxels"
            
            # cp -r source_dir target_path
            try:
                shutil.copytree(source_voxel_dir, target_path)
            except Exception as e:
                print(f"无法复制文件夹: {source_voxel_dir} 到 {target_path}. 错误: {e}")

            # print(f"target_path: {target_path}")
            # cp -r 

                
            

def main():
    parser = argparse.ArgumentParser(description="复制当前目录下的子文件夹到目标目录。")
    # parser.add_argument("target_dir", type=str, help="目标目录路径")
    parser.add_argument("--overwrite", action="store_true", help="如果目标目录存在同名文件夹，是否覆盖")
    args = parser.parse_args()
    
    current_dir = "/drone_occ/OccDepth/data/kitti/dataset_odometry_voxels/dataset/sequences/"
    target_dir = "/drone_occ/OccDepth/data/kitti/odometry/dataset/sequences"
    
    print(f"源目录: {current_dir}")
    print(f"目标目录: {target_dir}")
    
    copy_subfolders(current_dir, target_dir, overwrite=False)

if __name__ == "__main__":
    main()