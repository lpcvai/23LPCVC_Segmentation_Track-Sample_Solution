from argparse import ArgumentParser, Namespace
from typing import List


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
        "--ouput",
        required=True,
        help="Filepath of where to store output segmentation map",
    )

    return parser.parse_args()


def main() -> None:
    args: Namespace = getArgs()
    pass
