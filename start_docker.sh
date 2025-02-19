# get current working directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
docker run -it --gpus all --runtime=nvidia --net=host \
    --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev:/dev\
    --name="OccDepth_dev" \
    -v ${SCRIPT_DIR}:/occdepth \
    -v /home/dji/hdd:/dataset \
    -v /home/dji/uav_group_private:/uav_group_private \
    -v /home/dji/uav_group_sharespace:/uav_group_sharespace \
    cuda11_7_pytorch_occ:occdepth_dev  \
    /bin/bash