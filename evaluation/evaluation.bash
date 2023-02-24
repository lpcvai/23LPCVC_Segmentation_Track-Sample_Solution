#!/bin/bash

mkdir evalDirectory

testImagesDirectory="test/IMG"
testGroundTruthImagesDirectory="test/GT"

testImages=$(ls $testImagesDirectory)

# Computes the speed of the model
for testImage in $testImages;
do
    python3.10 solution.pyz -i ${testImagesDirectory}/${testImage} -o evalDirectory/${testImage}
    speed=$[${speed} + ${SECONDS}]
done;

python3.10 accuracy.py -i ${evalDirectory} -g ${testGroundTruthImagesDirectory}

rm -rf evalDirectory
echo "Speed: ${speed}"
