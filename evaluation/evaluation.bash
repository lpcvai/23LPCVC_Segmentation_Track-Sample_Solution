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

time_output=$(timeout $TIMEOUT python3.6 $solution -i ${testImagesDirectory} -o $eval ; 2>&1 > /dev/null )
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
    real_time=$(echo "$time_output")
    echo "$real_time"
    
    mdice=$(python3.6 $scoreResults -i $eval -g ${testGroundTruthImagesDirectory} 2>/dev/null)
    accuracy_exit_code=$?
    if [ $accuracy_exit_code -eq 1 ]; then
	echo "Solution could not be scored"
	mean_dice=99999999999
	mean_speed=99999999999
	score=99999999999
	exit_code=1
    else	
    	mean_speed=$( echo "$real_time / $count" | bc -l)
    	mean_dice=$mdice
    	score=$( echo "$mean_dice / $mean_speed" | bc -l)
    	exit_code=0
    fi
fi

echo "Mean Dice: ${mean_dice}"
echo "Mean Execution (seconds) ${mean_speed}"
echo "Calulated Score: ${score}"

json='{"mean_dice":"'${mean_dice}'","mean_speed":"'${mean_speed}'","score":"'${score}'"}'
echo "$json" > $path/output/$submissionName.json
echo "$submissionName"
rm -rf $eval
exit $exit_code
