#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate DSNeRF

python run_nerf.py --config configs/cupA.txt --render_only --white_bkgd
python run_nerf.py --config configs/orangeA.txt --render_only --white_bkgd
python run_nerf.py --config configs/broccoliA.txt --render_only --white_bkgd
python run_nerf.py --config configs/teddybearA.txt --render_only --white_bkgd
python run_nerf.py --config configs/backpackA.txt --render_only --white_bkgd
