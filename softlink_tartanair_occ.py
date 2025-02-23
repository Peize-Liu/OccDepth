import os

TARTANAIROCC_BASE = "/uav-nas/SharedDatasets/TartanAirKittiOcc"
TARGET_BASE = "/home/pliuan/6dof-occ/OccDepth/data/TartanAirOcc/dataset/sequences"

subdir = ["amusement", "gascola", "neighborhood", "oldtown", "seasonsforest"] # do not change the order; preprocess script depends on this order
max_sequence = 5

def main():
    print("Creating softlinks for TartanAirOcc dataset\n")
    reindex = 0
    for i in range(max_sequence):
        for j in range(len(subdir)):
            format_reindex = f"{reindex:02d}"
            print(f"Processing {subdir[j]} sequence {i}")
            format_seq = f"{i:02d}"
            source_dir = TARTANAIROCC_BASE + "/" + subdir[j] + "/" + format_seq
            targetdir = TARGET_BASE + "/" + format_reindex
            # ln -s source_dir targetdir
            if not os.path.exists(source_dir):
                print(f"Source directory {source_dir} does not exist")
                continue
            os.symlink(source_dir, targetdir)
            if os.path.islink(targetdir):
                print(f"Softlink created: {targetdir}")
            reindex += 1

if __name__ == "__main__":
    main()