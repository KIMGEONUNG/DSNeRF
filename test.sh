#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate DSNeRF

if [[ -z $1 ]]; then
  echo -e "\033[31mError: specify config as 'configs/bear.txt' \033[0m" >&2
  exit 1
fi

python run_nerf.py --config $1 --render_only --white_bkgd
