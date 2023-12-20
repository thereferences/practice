#!/bin/bash

: << 'comment'
The set up herein is in line with the Dockerfile set up.  Both use the same
requirements.txt file to create an environment.
comment

# The environment in focus
prefix=/mnt/j/programs/anaconda3/envs/practice

: << 'delete'
  Delete the existing <practice> environment
delete
conda remove -y --prefix $prefix --all

: << 'rebuild'
  Rebuild environment <practice> via environment.yml
rebuild
conda env create -f environment.yml -p $prefix
# conda create -y --prefix $prefix -c conda-forge  python==3.11.7
# conda activate development
# conda install -y --prefix $prefix -c conda-forge --file requirements.txt