from argparse import ArgumentParser, Namespace
from accuracy import *
from typing import List, Tuple

import cv2
import numpy
#import torch
#import torch.nn.functional as F
from cv2.mat_wrapper import Mat
from imageio.core.util import Array
from imageio import imread
from numpy import ndarray
import sys

SIZE: List[int] = [512, 512]

def getArgs() -> Namespace:
    # NOTE: These variables can be changed
    programName: str = "LPCVC 2023 Sample Solution"
    authors: List[str] = ["Nicholas M. Synovic", "Ping Hu"]

    prog: str = programName
    usage: str = f"This is the {programName}"
    description: str = f"This {programName} does create a single segmentation map of arieal scenes of disaster environments captured by unmanned arieal vehicles (UAVs)"
    epilog: str = f"This {programName} was created by {''.join(authors)}"

    # NOTE: It is recommended to not change these flags
    parser: ArgumentParser = ArgumentParser(prog, usage, description, epilog)
    parser.add_argument(
        "-i",
        "--image",
        required=True,
        help="Filepath to generated segmentation map",
    )
    parser.add_argument(
        "-g",
        "--groundtruth",
        required=True,
        help="Filepath to ground truth to compare to",
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
    print(get_score(args.image, args.groundtruth))


if __name__=='__main__':
    main()