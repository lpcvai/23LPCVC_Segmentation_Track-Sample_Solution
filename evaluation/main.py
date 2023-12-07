from argparse import ArgumentParser, Namespace
from accuracy import *
from typing import List, Tuple

import cv2
import numpy
from cv2.mat_wrapper import Mat
from imageio.core.util import Array
from imageio import imread
from numpy import ndarray
import sys
import os
import glob

SIZE: List[int] = [512, 512]

def getArgs() -> Namespace:
    # NOTE: These variables can be changed
    programName: str = "LPCVC 2023 Sample Solution"
    authors: List[str] = ["Stephanie Guerra", "Himank Kothari", "Sai Vemu"]

    prog: str = programName
    usage: str = f"This is the {programName}"
    description: str = f"This {programName} does create a single segmentation map of aerial scenes of disaster environments captured by unmanned arieal vehicles (UAVs)"
    epilog: str = f"This {programName} was created by {''.join(authors)}"

    # NOTE: It is recommended to not change these flags
    parser: ArgumentParser = ArgumentParser(prog, usage, description, epilog)
    parser.add_argument(
        "-i",
        "--imagedirectory",
        required=True,
        help="Directory containing the generated segmentation maps",
    )
    parser.add_argument(
        "-g",
        "--groundtruth",
        required=True,
        help="Directory containing the ground truth images to compare to",
    )

    return parser.parse_args()

def loadGroundTruthImage(imagePath: str) -> ndarray:
    image: Array = imread(uri=imagePath).astype(numpy.uint8)

    if len(image.shape) == 3:
        image = image[:, :, 0]

    resizedImage: Mat = cv2.resize(image, tuple(SIZE), interpolation=cv2.INTER_AREA)
    resizedImage: Mat = cv2.resize(
        resizedImage, tuple(SIZE), interpolation=cv2.INTER_NEAREST
    )
    outputImage: ndarray = resizedImage[numpy.newaxis, :, :]

    return outputImage

def get_score(image, groundTruth):
    accuracyTracker: AccuracyTracker = AccuracyTracker(n_classes=14)
    groundTruthArray: ndarray = loadGroundTruthImage(imagePath=groundTruth)
    outArray: ndarray = loadGroundTruthImage(imagePath=image)
    accuracyTracker.update(groundTruthArray, outArray)
    accuracyTracker.get_scores()
    return accuracyTracker.mean_dice

def main():
    args: Namespace = getArgs()
    
    segmentation_map_directory = args.imagedirectory
    ground_truth_directory = args.groundtruth
    
    segmentation_maps = sorted(glob.glob(os.path.join(segmentation_map_directory, '*.png')))
    ground_truths = sorted(glob.glob(os.path.join(ground_truth_directory, '*.png')))
    
    if len(segmentation_maps) != len(ground_truths):
        print("The number of segmentation maps and ground truth images does not match.")
        sys.exit(1)

    total_score = 0
    image_count = len(segmentation_maps)

    for image, ground_truth in zip(segmentation_maps, ground_truths):
        score = get_score(image, ground_truth)
        total_score += score

    average_score = total_score / image_count
    print(f"{average_score}")


if __name__=='__main__':
    main()
