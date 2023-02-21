#!/bin/bash

CUDA_VISIBLE_DEVICES=0
source ~/anaconda3/etc/profile.d/conda.sh
conda activate DSNeRF

python run_nerf.py --config configs/fern_2v_cp.txt
