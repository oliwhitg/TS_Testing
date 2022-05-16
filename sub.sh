#!/bin/csh
#$ -j y
#$ -o .
#$ -l s_rt=700:00:00
#$ -l h_rt=700:00:00
#$ -N salts_sub

CURRENTRUN=0
for i in $(seq 1 100);
do 
    echo $i
    
    if [ -d "~/TS_Test_Environment/run_$i" ]; then
        CURRENTRUN=$i
    fi
done

echo $CURRENTRUN
set fromdir = $(pwd)
set todir = $(pwd)/run_$CURRENTRUN
#setenv WORK /tmp/$USER/$JOB_ID

echo $fromdir
echo $todir

#mkdir -p $todir
#
#mkdir -p $WORK
#cd $fromdir
#cp -r * $WORK
#cd $WORK
#./combined_tersoff_3d_lj_D_zmove6000_harm_nodrsav_lin_2021.x
#cp *.dat *.log $fromdir
#cp * $todir
#rm -Rf $WORK
