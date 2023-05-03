### LPCVC2023 Sample Solution

## How to Run

The following sections cover how to evaluate the sample solution.

## Directory Structure

Here is the directory structure that will be used to evaluate solutions. The test directory will need to be created.
#### Note: The solution.pyz stored here was developed with map_location=torch.device('cuda') as in the main function in solution/main.py.
```
evaluation
├── accuracy.py
├── evaluation.bash
├── main.py
├── README.md
├── solution.pyz
└── test
    ├── GT
    │   ├── img_0000.png
    │   └── img_0001.png
    └── IMG
        ├── img_0000.png
        └── img_0001.png
```
## Metrics
- Accuracy will be measured using the Accuracy.py script. In this script we make a NclassxNclass Confusion matrix out of the inputted segmentation map and ground truth. This confusion matrix is used to calculate the dice coefficient.

- Speed will be measured based upon the execution time of solution.pyz / numImages.

## Execution
In order to run the evaluation script we will be running use `./evaluation.bash solution.pyz` this will produce an output file with the scoring metrics.

In order to only test the dice coefficient of individually:
`python3.6 main.py -i /path/to/segmentedDirectory -g /path/to/groundtruthDirectory`
