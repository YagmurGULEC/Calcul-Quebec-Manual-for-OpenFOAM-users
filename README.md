# Calcul-Quebec-Manual-for-OpenFOAM-users


User manual for Calcul Quebec Mammouth-Mp2b and helpful codes to send and transfer from the server
This manual is prepared especially to run OpenFOAM cases in Mammouth-Mp2b administered by Calcul-Quebec. Besides, there are some helpful scripts to send and transfer 
multiple cases.

The Linux codes shared were tested only in Mammouth-Mp2b.

For basics to use the you may go through the link below:
https://wiki.ccs.usherbrooke.ca/Mammouth-Mp2b

For applying to have an account, you better have a look at the link: https://www.computecanada.ca/research-portal/account-management/apply-for-an-account/.


Every time you would like to connect to the remote server to exchange files, you need to enter the password. Instead, you may look at ssh connection with keygen 
to make automization easier. There is an useful note you may wish to check.

https://github.com/deekshaarya4/CalculQuebecNotes/blob/master/connect_to_server.md
Or you can follow the steps explained clearly in https://www.youtube.com/watch?v=vpk_1gldOAE&ab_channel=CoreySchafer.

The script mpi_job.sh is to run the case in question. This file should be in your case directory. 

The script AllToServer is written to automize the process of preparing multiple cases (blockMesh, refineMesh and decomposePar). After making them ready, it sends them to the server, 
and save them in the directory intented.


The script AllFromServer is for  the automization of transfering case directories to your local machine to post-process the results.

You need to load several modules to run any OpenFOAM case, depending on which version you would like to use. 
For OpenFOAM 2.3.1,
module purge
module load nixpkgs/16.09  gcc/4.8.5  openmpi/2.1.1
module load openfoam/2.3.1

For other versions you may check if they are installed already in the solver. 
module avail openfoam 

The modules needed to use OpenFOAM appears after writing module spider openfoam/2.3.1.

For parallel runs, it may take a lot of time to reconstruct the data. Instead, you may extract csv files with AllFromServerCsv without waiting for reconstructPar.


