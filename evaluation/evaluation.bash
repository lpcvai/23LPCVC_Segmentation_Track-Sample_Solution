#!/bin/bash

mkdir evalDirectory

testImagesDirectory="test/IMG"
testGroundTruthImagesDirectory="test/GT"

testImages=$(ls $testImagesDirectory)
dice=0
speed=0
count=0
# Computes the speed of the model
for testImage in $testImages;
do
    #python3.6 solution.pyz -i ${testImagesDirectory}/${testImage} -o evalDirectory/${testImage}
    ((count++))
    time_output=$( { time python3.6 solution.pyz -i ${testImagesDirectory}/${testImage} -o evalDirectory/${testImage} ; } 2>&1 >/dev/null )
    real_time=$( echo "$time_output" | grep "real" | awk -F"m" '{print $2}' | awk -F"s" '{print $1}')
    speed=$( echo "$speed + $real_time" | bc)
    result=$(python3.6 evaluation.py "evalDirectory/${testImage}" "${testGroundTruthImagesDirectory}/${testImage}")
    dice=$( echo "$dice + $result" | bc)
done;
avg_speed=$( echo "$speed / $count" | bc -l)
avg_dice=$( echo "$dice / $count" | bc -l)
score=$( echo "$avg_dice / $avg_speed" | bc -l)
echo "${score}"
#python3.10 accuracy.py -i ${evalDirectory} -g ${testGroundTruthImagesDirectory}

rm -rf evalDirectory

