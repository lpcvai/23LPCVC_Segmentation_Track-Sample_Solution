from argparse import ArgumentParser, Namespace
from typing import List, Tuple, BinaryIO
import numpy as np
from PIL import Image
import torch
import torch.nn.functional as F
from torchvision.transforms import transforms
from utils.fanet import FANet
import cv2
from imageio import imread
from cv2.mat_wrapper import Mat
import pkg_resources
import sys
import os
import io
import zipfile 
import pkg_resources
import time
SIZE: List[int] = [512, 512]


def getArgs() -> Namespace:
    # NOTE: These variables can be changed
    programName: str = "LPCVC 2023 Sample Solution"
    authors: List[str] = ["Benjamin Boardley","Nicholas M. Synovic", "Ping Hu"]

    prog: str = programName
    usage: str = f"This is the {programName}"
    description: str = f"This {programName} does create a single segmentation map of arieal scenes of disaster environments captured by unmanned arieal vehicles (UAVs)"
    epilog: str = f"This {programName} was created by {''.join(authors)}"

    # NOTE: Do not change these flags
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
        help="Filepath to the corresponding output segmentation map",
    )

    return parser.parse_args()


def loadImageToTensor(imagePath: str) -> torch.Tensor:
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

def main() -> None:
    args: Namespace = getArgs()

    # NOTE: modelPath should be the path to your model in respect to your solution directory
    modelPath: str = "model.pkl"

    image_files: List[str] = os.listdir(args.input)

    with pkg_resources.resource_stream(__name__, modelPath) as model_file:
        model: FANet = FANet()
        device = torch.device("cuda")
        model.to(device)
        model.load_state_dict(
                state_dict=torch.load(f=model_file, map_location=torch.device("cuda")), strict=False
        )
        model.eval()
        start, end = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)

        #Warm Up
        for image_file in image_files[:15]:
            input_image_path: str = os.path.join(args.input, image_file)
            imageTensor: torch.Tensor = loadImageToTensor(imagePath=input_image_path)
            imageTensor = imageTensor.to(device)
            outTensor: torch.Tensor = model(imageTensor)

        time = 0
        with torch.no_grad():
            for image_file in image_files:
                input_image_path: str = os.path.join(args.input, image_file)
                output_image_path: str = os.path.join(args.output, image_file)
                imageTensor: torch.Tensor = loadImageToTensor(imagePath=input_image_path)
                imageTensor = imageTensor.to(device)
                start.record()
                outTensor: torch.Tensor = model(imageTensor)
                end.record()
                torch.cuda.synchronize()

                time += start.elapsed_time(end)
                
                outTensor: torch.Tensor = F.interpolate(
                    outTensor, SIZE, mode="bilinear", align_corners=True
                )

                outArray: np.ndarray = outTensor.cpu().data.max(1)[1].numpy()
                outArray: np.ndarray = outArray.astype(np.uint8)

                outImage: np.ndarray = np.squeeze(outArray, axis=0)
                outImage = Image.fromarray(outImage, mode='L')
                outImage.save(output_image_path)
        print(time/1000)
        del model
        del imageTensor
        del outTensor
        torch.cuda.empty_cache()
        model_file.close()

