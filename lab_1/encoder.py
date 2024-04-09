import argparse
import logging
import os
import sys


project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from r_wr_funcs import read_txt, save_txt, save_json
from utils.constants import ALPHABET


def encode(input_file: str, output_file: str, output_json_file: str, shift: int):

    alf = ALPHABET["rus_alf"]

    """
    Encoding text from input_file with cesar's chipher with alphabet rotated by 'shift' times
    """

    res: str = ""

    s = read_txt(input_file)
    s = s.upper()

    encoded_alf: str = alf[shift:] + alf[:shift]

    encoded_dict = dict()

    for i, j in zip(encoded_alf, alf):
        encoded_dict[j] = i
    
    for i in s:
        res += encoded_dict.get(i, i)

    save_txt(output_file, res)
    save_json(output_json_file, encoded_dict)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = encode.__doc__)
    parser.add_argument("input_file", type = str, help = "Input file name")
    parser.add_argument("output_file", type = str, help = "Output file name")
    parser.add_argument("output_json_file", type = str, help = "Output key file name")
    parser.add_argument('shift', type = int, help = 'alphabet shift parametrization')

    args = parser.parse_args()

    logging.basicConfig(
    level=logging.DEBUG,
    format='[{asctime}] #{levelname:8} {filename}:'
           '{lineno} - {name} - {message}',
    style='{'
)

    logger = logging.getLogger(__name__)

    encode(args.input_file, args.output_file, args.output_json_file, args.shift)