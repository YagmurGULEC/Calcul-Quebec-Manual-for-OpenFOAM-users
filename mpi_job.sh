#!/bin/bash
#SBATCH --account=accountname#name your supervisor account
#SBATCH --time=0-72:00#time needed for the run
#SBATCH --nodes=1#I think you dont need to modify this.
#SBATCH --ntasks-per-node=4#the numbers of subdomain obtained by decomposePar
#SBATCH --mem-per-cpu=1291M#I think you dont need to modify this.
#SBATCH --job-name=test
#SBATCH --output=%x-%j.out
#SBATCH --error=error-%j.out

module purge
module load nixpkgs/16.09  gcc/4.8.5  openmpi/2.1.1
module load openfoam/2.3.1
mpirun -np 4 solvername -parallel>&log
