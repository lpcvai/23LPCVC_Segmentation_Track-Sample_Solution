from argparse import ArgumentParser, Namespace
from pathlib import PurePath
from typing import List, Tuple

import cv2
import numpy
import torch
import torch.nn.functional as F
from cv2.mat_wrapper import Mat
from imageio.core.util import Array
from imageio.v2 import imread
from numpy import ndarray
from torch import Tensor
from torchvision.transforms import transforms
from torchvision.utils import save_image
from utils.fanet import FANet

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
        "--input",
        required=True,
        help="Filepath to an image to create a segmentation map of",
    )
    parser.add_argument(
        "-g",
        "--ground-truth",
        required=True,
        help="Filepath the corresponding ground truth segmentation map to compare against",
    )

    return parser.parse_args()


def loadImageToTensor(imagePath: str) -> Tensor:
    MEAN: Tuple[float, float, float] = (0.485, 0.456, 0.406)
    STANDARD_DEVIATION: Tuple[float, float, float] = (0.229, 0.224, 0.225)

    image: Array = imread(uri=imagePath)
    resizedImage: Mat = cv2.resize(image, tuple(SIZE), interpolation=cv2.INTER_AREA)
    imageTensor: Tensor = transforms.ToTensor()(resizedImage)
    imageTensor: Tensor = transforms.Normalize(mean=MEAN, std=STANDARD_DEVIATION)(
        imageTensor
    )
    imageTensor: Tensor = imageTensor.unsqueeze(0)

    return imageTensor


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


def main() -> None:
    args: Namespace = getArgs()

    # NOTE: modelPath should be the path to your model
    modelPath: str = "model.pkl"

    imageTensor: Tensor = loadImageToTensor(imagePath=args.input)
    groundTruthImage: ndarray = loadGroundTruthImage(imagePath=args.ground_truth)

    model: FANet = FANet()
    model.load_state_dict(state_dict=torch.load(f=modelPath))
    model.eval()
    # model.cuda()

    outTensor: Tensor = model(imageTensor)
    outTensor: Tensor = F.interpolate(
        outTensor, SIZE, mode="bilinear", align_corners=True
    )

    outTensor = outTensor.cpu().data.max(1)[1].numpy()

    pass
