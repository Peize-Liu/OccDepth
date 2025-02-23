import io_data as SemanticKittiIO
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d


def check_label(path):
    label = SemanticKittiIO._read_label_SemKITTI(path)
    return label

def check_invalid(path):
    invalid = SemanticKittiIO._read_invalid_SemKITTI(path)
    return invalid

def check_occluded(path):
    occluded = SemanticKittiIO._read_occluded_SemKITTI(path)
    return occluded

# def visualize_label(label):
#     import matplotlib.pyplot as plt
#     plt.imshow(label)
#     plt.show()

def visualize_labels(voxel_labels,grid_size,voxel_size):
    # 计算体素的3D坐标
    indices = np.array(range(voxel_labels.size))  # 线性索引
    z_indices = indices // (grid_size[0] * grid_size[1])
    y_indices = (indices % (grid_size[0] * grid_size[1])) // grid_size[0]
    x_indices = (indices % (grid_size[0] * grid_size[1])) % grid_size[0]

    # 变换为实际3D坐标
    points = np.vstack((x_indices, y_indices, z_indices)).T * voxel_size

    # 只保留非零标签的体素进行可视化（可选）
    # mask = voxel_labels > 0  # 过滤掉 label=0 的背景
    # points = points[mask]
    # labels = voxel_labels[mask]
    labels = voxel_labels

    # 使用 colormap 生成颜色
    cmap = plt.get_cmap("viridis")  # 选择 colormap
    norm_labels = labels / 70.0  # 归一化到 [0,1]
    colors = cmap(norm_labels)[:, :3]  # 获取 RGB 颜色

    # 创建 Open3D 点云对象
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    # 可视化
    o3d.visualization.draw_geometries([pcd], window_name="Voxel Visualization")

def main():
    label = check_label("/home/pliuan/6dof-occ/OccDepth/data/TartanAirOcc/00/voxels/000000.label")
    invalid = check_invalid("/home/pliuan/6dof-occ/OccDepth/data/TartanAirOcc/00/voxels/000000.invalid")
    occluded = check_occluded("/home/pliuan/6dof-occ/OccDepth/data/TartanAirOcc/00/voxels/000000.occluded")
    # print(label)
    # print(invalid)
    # print(occluded)
    visualize_labels(label,(256,256,256),0.25)


if __name__ == "__main__":
    main()


