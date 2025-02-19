#!/bin/bash
workdir=$(cd $(dirname $0); pwd)
echo "workdir:" $workdir

<<<<<<< HEAD
export DATA_LOG=$workdir/logdir/test
export DATA_CONFIG=$workdir/occdepth/config/semantic_kitti/multicam_flospdepth_crp_stereodepth_cascadecls_2080ti.yaml
=======
export DATA_LOG=$workdir/logdir/b3_F32_FixMultiview
<<<<<<< HEAD
export DATA_CONFIG=/drone_occ/OccDepth/occdepth/config/semantic_kitti/multicam_flospdepth_crp_stereodepth_cascadecls_2080ti.yaml
>>>>>>> b90777a (adjust for local environment)
=======
export DATA_CONFIG=/occdepth/occdepth/config/semantic_kitti/multicam_flospdepth_crp_stereodepth_cascadecls_2080ti.yaml
>>>>>>> ea3613b (Initialize For tarttanAir)
export PYTHONPATH=$workdir:$PYTHONPATH
export ETS_TOOLKIT=qt4
export QT_API=pyqt5
