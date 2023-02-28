if [[ $(hostname | grep mark13) ]]; then
    # IN DOCKER CONTAINER MARK13
    export CUDA_VISIBLE_DEVICES=0
    export condapath=/opt/conda/etc/profile.d/conda.sh
else
    # IN LOCAL SYSTEM
    export CUDA_VISIBLE_DEVICES=0
    export condapath=$HOME/anaconda3/etc/profile.d/conda.sh
fi
