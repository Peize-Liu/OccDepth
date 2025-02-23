import numpy as np
from tqdm import tqdm
import os
import glob
import hydra
from omegaconf import DictConfig
import occdepth.data.semantic_kitti.io_data as SemanticKittiIO
from hydra.utils import get_original_cwd
from occdepth.data.NYU.preprocess import _downsample_label
from multiprocessing import Pool, cpu_count

def process_sequence(sequence, config, remap_lut, scene_size):
    """ 处理单个 sequence 并保存结果 """
    sequence_path = os.path.join(config.data_root, sequence)
    label_paths = sorted(glob.glob(os.path.join(sequence_path, "voxels", "*.label")))
    invalid_paths = sorted(glob.glob(os.path.join(sequence_path, "voxels", "*.invalid")))
    out_dir = os.path.join(config.data_preprocess_root, "labels", sequence)
    os.makedirs(out_dir, exist_ok=True)

    downscaling = {"1_1": 1, "1_8": 8}

    for i in tqdm(range(len(label_paths)), desc=f"Processing sequence {sequence}"):
        frame_id, extension = os.path.splitext(os.path.basename(label_paths[i]))

        LABEL = SemanticKittiIO._read_label_SemKITTI(label_paths[i])
        INVALID = SemanticKittiIO._read_invalid_SemKITTI(invalid_paths[i])
        LABEL = remap_lut[LABEL.astype(np.uint16)].astype(np.float32)  # Remap 20 classes semanticKITTI SSC
        LABEL[np.isclose(INVALID, 1)] = 255  # Setting to unknown all voxels marked on invalid mask...
        LABEL = LABEL.reshape(scene_size)

        for scale in downscaling:
            filename = frame_id + "_" + scale + ".npy"
            label_filename = os.path.join(out_dir, filename)
            # If files have not been created...
            if not os.path.exists(label_filename):
                if scale == "1_8":
                    LABEL_ds = _downsample_label(LABEL, scene_size, downscaling[scale])
                else:
                    LABEL_ds = LABEL
                np.save(label_filename, LABEL_ds)
                print("Wrote to", label_filename)

config_path = os.getenv('DATA_CONFIG')

@hydra.main(config_name=config_path)
def main(config: DictConfig):
    scene_size = (256, 256, 256)
    sequences = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"]
    remap_lut = SemanticKittiIO.get_remap_lut(
        os.path.join(get_original_cwd(), "occdepth", "data", "semantic_kitti", "semantic-kitti.yaml")
    )

    num_processes = min(20, len(sequences))  # 限制最多 10 个进程
    print(f"Starting {num_processes} parallel processes...")

    # 使用多进程，每个进程处理 1 个 sequence
    with Pool(processes=num_processes) as pool:
        pool.starmap(process_sequence, [(seq, config, remap_lut, scene_size) for seq in sequences])

if __name__ == "__main__":
    main()