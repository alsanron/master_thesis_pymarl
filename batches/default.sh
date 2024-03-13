#!/bin/bash
#SBATCH --job-name=cpu
#SBATCH --output=cpu-%j.log
#SBATCH --time=06:00:00
#SBATCH --partition=regular
#SBATCH --mem=8GB
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --partition=regular

source ~/venvs/pymarl_gputest/bin/activate
module load Python/3.8.16-GCCcore-11.2.0
module load SciPy-bundle/2023.07-gfbf-2023a
module load PyTorch/1.12.1-foss-2022a-CUDA-11.7.0

python3 src/main.py --config=qmix --env-config=sc2 with env_args.map_name=3m
