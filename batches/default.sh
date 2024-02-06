#!/bin/bash
#SBATCH --job-name=default_job
#SBATCH --output=job-%j.log
#SBATCH --time=10:00:00
#SBATCH --partition=gpu
#SBATCH --gres=1
#SBATCH --mem=16GB



#SBATCH --nodes=1
#SBATCH --ntasks=1 #
#SBATCH --cpus-per-task=16 
#SBATCH --partition=regular

source ../venvs/pymarl/bin/activate
python3 src/main.py --config=vdn --env-config=sc2 with env_args.map_name=3m
