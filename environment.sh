#!/bin/bash

: << 'comment'
The set up herein is in line with the Dockerfile set up.  Both use the same
requirements.txt file to create an environment.
comment

# The environment in focus
prefix=/mnt/j/programs/anaconda3/envs/development

: << 'delete'
  Delete the existing <development> environment
delete
conda remove -y --prefix $prefix --all

: << 'rebuild'
  Rebuild environment <development> via a requirements.txt file
rebuild
conda create -y --prefix $prefix -c conda-forge  python==3.11.7
conda activate development
conda install -y --prefix $prefix -c conda-forge --file requirements.txt