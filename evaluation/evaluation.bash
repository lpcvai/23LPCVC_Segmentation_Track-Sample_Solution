#!/bin/bash

mkdir evalDirectory

testImagesDirectory="test/IMG"
testGroundTruthImagesDirectory="test/GT"

testImages=$(ls $testImagesDirectory)
summed_dice=0
total_time=0
count=0

for testImage in $testImages;
do
    ((count++))
    time_output=$( { time python3.6 solution.pyz -i ${testImagesDirectory}/${testImage} -o evalDirectory/${testImage} ; } 2>&1 >/dev/null )
    real_time=$( echo "$time_output" | grep "real" | awk -F"m" '{print $2}' | awk -F"s" '{print $1}')
    total_time=$( echo "$total_time + $real_time" | bc)
    mdice=$(python3.6 main.py -i evalDirectory/${testImage} -g ${testGroundTruthImagesDirectory}/${testImage} 2>/dev/null)
    summed_dice=$( echo "$summed_dice + $mdice" | bc)
done;

mean_speed=$( echo "$total_time / $count" | bc -l)
mean_dice=$( echo "$summed_dice / $count" | bc -l)
score=$( echo "$mean_dice / $mean_speed" | bc -l)

echo "Mean Dice: ${mean_dice}"
echo "Mean Execution (seconds) ${mean_speed}"
echo "Calulated Score: ${score}"

json='{ "mean_dice": "'${mean_dice}'", "mean_speed": "'${mean_speed}'", "score": "'${score}'" }'
echo "$json" > output/output.json

rm -rf evalDirectory

