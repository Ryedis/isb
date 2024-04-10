import argparse
import os
import sys


project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from utils.r_wr_funcs import read_txt, save_txt, read_json
from utils.constants import ALPHABET


def decode(input_file: str, output_file: str, key_json_file: str) -> None:
    """
    Decoding text from input file with given key

    Args:
    input_file: path to text to decode
    output_file: path to decoded text
    key_json_file: path to key
    """
    key = read_json(key_json_file)
    s = read_txt(input_file)
    res: str = ""
    for i in s:
        if i in key:
            res += key.get(i,i)
    
    save_txt(output_file, res)


def main() -> None:
    """
    Uses argparse to process command-line arguments
    and calls the decode() function to decode data.
    """
    parser = argparse.ArgumentParser(description = decode.__doc__)
    parser.add_argument("input_file", type = str, help = "Input file name")
    parser.add_argument("output_file", type = str, help = "Output file name")
    parser.add_argument("key_file", type = str, help = "File with key to decode")

    args = parser.parse_args()

    decode(args.input_file, args.output_file, args.key_file)


if __name__ == "__main__":
    main()
#python decoder.py task_2\origin.txt task_2\decode.txt task_2\key.json