from accuracy import *
from typing import List, Tuple

import cv2
import numpy
import torch
import torch.nn.functional as F
from cv2.mat_wrapper import Mat
from imageio.core.util import Array
from imageio import imread
from numpy import ndarray
import sys

SIZE: List[int] = [512, 512]

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

if __name__=='__main__':
    print(get_score(sys.argv[1], sys.argv[2]))