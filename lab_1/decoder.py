import argparse
import os
import sys


project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from utils.r_wr_funcs import read_txt, save_txt, read_json
from utils.constants import ALPHABET


def read_key_json(key_json_file: str) -> dict:
    """
    Read key from .json file

    Args:
    key_json_file: path to key json file
    Returns:
    Dictionary containing the key
    """
    return read_json(key_json_file)


def decode(input_file: str, output_file: str, key: str) -> None:
    """
    Decoding text from input file with given key

    Args:
    input_file: path to text to decode
    output_file: path to decoded text
    key_json_file: path to key
    """
    s = read_txt(input_file)
    res: str = ""
    try:
        for i in s:
            if i in key:
                res += key.get(i,i)
    except Exception as e:
        print("An error occurred while processing the data:", e)
    
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
    key = read_key_json(args.key_file)

    decode(args.input_file, args.output_file, key)


if __name__ == "__main__":
    main()
#python decoder.py task_2\origin.txt task_2\decode.txt task_2\key.json