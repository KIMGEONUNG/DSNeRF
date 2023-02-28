#!/bin/bash

source config.sh
source $condapath
conda activate DSNeRF

python run_nerf.py --config configs/co3d.txt
