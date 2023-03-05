#!/bin/bash

source config.sh
source $condapath
conda activate DSNeRF

if [[ -z $1 ]]; then
  echo -e "\033[31mError: no config path \033[0m" >&2
  exit 1
fi

if ! [[ -f $1 ]]; then
  echo -e "\033[31mError: no such file $1  \033[0m" >&2
  exit 1
fi

python run_nerf.py --config $1
