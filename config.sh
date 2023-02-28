if [[ $(hostname | grep mark13) ]]; then
    # IN DOCKER CONTAINER MARK13
    if [[ -z $CUDA_VISIBLE_DEVICES ]]; then
      export CUDA_VISIBLE_DEVICES=0
    fi
    export condapath=/opt/conda/etc/profile.d/conda.sh
else
    if [[ -z $CUDA_VISIBLE_DEVICES ]]; then
      export CUDA_VISIBLE_DEVICES=0
    fi
    export condapath=$HOME/anaconda3/etc/profile.d/conda.sh
fi
