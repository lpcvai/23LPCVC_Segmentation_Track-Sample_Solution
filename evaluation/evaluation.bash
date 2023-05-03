#!/bin/bash

# Add a variable for the timeout in seconds (15 minutes = 900 seconds)
TIMEOUT=900

solution=$1
filename=$(basename $solution)
submissionName=${filename%.pyz}

path="/home/lpcvcnode1/lpcvc2023/evaluation"
mkdir $path/evalDirectory
if [ ! -d "$path/output" ]; then
  mkdir "$path/output"
fi
eval=$path/evalDirectory

scoreResults="$path/main.py"
testImagesDirectory="$path/LPCVC_Test_Private/LPCVC_Test_Private/IMG"
testGroundTruthImagesDirectory="$path/LPCVC_Test_Private/LPCVC_Test_Private/GT"
testImages=$(ls $testImagesDirectory)
summed_dice=0
count=600

# Run the solution with a timeout
time_output=$( { time timeout $TIMEOUT python3.6 $solution -i ${testImagesDirectory} -o $eval ; } 2>&1 > /dev/null )
exit_code=$?
python3.6 clear_gpu.py
if [ $exit_code -eq 124 ]; then
    # The solution took too long to run (> 15 minutes)
    echo "Solution timed out"
    mean_dice=99999999999
    mean_speed=-1
    score=99999999999
    exit_code=2
elif [ $exit_code -ne 0 ]; then
    # The solution failed to run
    echo "Solution failed to run"
    mean_dice=99999999999
    mean_speed=99999999999
    score=99999999999
    exit_code=1
else
    # The solution ran successfully; calculate the scores
    real_time=$(echo "$time_output" | grep -oP '^real\s+\K[0-9]*h?[0-9]+m[0-9.]+s')
    hours=$(echo "$real_time" | grep -oP '^\d+(?=h)')
    if [ -z "$hours" ]; then
        hours="0"
    fi
    minutes=$(echo "$real_time" | grep -oP '(?<=h)?\d+(?=m)')
    seconds=$(echo "$real_time" | grep -oP '\d+\.\d+(?=s)')
    real_time=$(echo "$hours * 3600 + $minutes * 60 + $seconds" | bc)
    echo "$real_time"
    #for testImage in $testImages;
    #do
        #((count++))
    mdice=$(python3.6 $scoreResults -i $eval -g ${testGroundTruthImagesDirectory} 2>/dev/null)
        #summed_dice=$( echo "$summed_dice + $mdice" | bc)
    #done;

    mean_speed=$( echo "$real_time / $count" | bc -l)
    mean_dice=$mdice #$( echo "$summed_dice / $count" | bc -l)
    score=$( echo "$mean_dice / $mean_speed" | bc -l)
    exit_code=0
fi

echo "Mean Dice: ${mean_dice}"
echo "Mean Execution (seconds) ${mean_speed}"
echo "Calulated Score: ${score}"

json='{"mean_dice":"'${mean_dice}'","mean_speed":"'${mean_speed}'","score":"'${score}'"}'
echo "$json" > $path/output/$submissionName.json
echo "$submissionName"

rm -rf $eval
exit $exit_code
