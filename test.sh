#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate DSNeRF

python run_nerf.py --config configs/co3d.txt --render_only
