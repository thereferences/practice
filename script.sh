#!/bin/bash

: << 'comment'
The set up herein is must be in line ...
comment

# The environment in focus
prefix=/mnt/j/programs/anaconda3/envs/practice

: << 'delete'
  Delete the existing <practice> environment
delete
conda remove -y --prefix $prefix --all

: << 'rebuild'
  Rebuild environment <development> via a requirements.txt file
rebuild
conda env create -f environment.yml -p $prefix