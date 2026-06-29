#!/bin/bash
#SBATCH --job-name=run2
#SBATCH --output=run2.out
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=a100
#SBATCH --cpus-per-task=4


# 激活你的新环境
source activate mechfind

# 运行你的脚本
python "5 do 3 after 4.py"
