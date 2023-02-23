from argparse import ArgumentParser, Namespace
from pathlib import PurePath
from typing import List

import cv2
import torch
import torchvision.transforms as transforms
from cv2.mat_wrapper import Mat
from imageio.core.util import Array
from imageio.v2 import imread
from utils.fanet import FANet


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
        "-o",
        "--output",
        required=True,
        help="Filepath of where to store output segmentation map",
    )

    return parser.parse_args()


def writeImage(imagePath: PurePath) -> None:
    pass


def main() -> None:
    args: Namespace = getArgs()

    SIZE: List[int] = [512, 512]

    # NOTE: modelPath should be the path to your model
    modelPath: str = "model.pkl"

    inputImage: Array = imread(uri=args.input)
    resizedInputImage: Mat = cv2.resize(
        inputImage, tuple(SIZE), interpolation=cv2.INTER_AREA
    )
    inputImageTensor = transforms.ToTensor()

    model: FANet = FANet()
    model.load_state_dict(state_dict=torch.load(f=modelPath))
    model.eval()
    model.cuda()

    pass
