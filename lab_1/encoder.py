import argparse
import os
import sys


project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from utils.r_wr_funcs import read_txt, save_txt, save_json
from utils.constants import ALPHABET


def encode(input_file: str, output_file: str, key_json_file: str, shift: int) -> None:
    """
    Encoding the text with the Caesar cipher

    Args:
        input_file: path .txt file
        output_file: path output .txt file
        key_json_file: path key .json file
        shift: how much does the alphabet shift
    """
    alf = ALPHABET["rus_alf"]
    res: str = ""

    s = read_txt(input_file)
    s = s.upper()

    encoded_alf: str = alf[shift:] + alf[:shift]

    encoded_dict = dict()

    for i, j in zip(encoded_alf, alf):
        encoded_dict[j] = i
    
    for i in s:
        res += encoded_dict.get(i, i)

    res = '"' + res + '"'

    save_txt(output_file, res)
    save_json(key_json_file, encoded_dict)


def main() -> None:
    """
    Uses argparse to process command-line arguments
    and calls the encode() function to encode data.
    """
    parser = argparse.ArgumentParser(description = encode.__doc__)
    parser.add_argument("input_file", type = str, help = "Input file name")
    parser.add_argument("output_file", type = str, help = "Output file name")
    parser.add_argument("key_json_file", type = str, help = "Output key file name")
    parser.add_argument('shift', type = int, help = 'alphabet shift parametrization')

    args = parser.parse_args()

    encode(args.input_file, args.output_file, args.output_json_file, args.shift)


if __name__ == "__main__":
    main()
#python encoder.py task_1\origin.txt task_1\encode.txt task_1\key.json 1