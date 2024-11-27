docker run -it --gpus all --runtime=nvidia --net=host \
    --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev:/dev\
    --name="OccDepth_test" \
    -v /home/dji/workspace/drone_occ:/drone_occ \
    -v /home/dji/hdd:/dataset \
    cuda11_7_pytorch_occ:occdepth  \
    /bin/bash