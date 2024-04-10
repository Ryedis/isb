import argparse
import os
import sys

from collections import Counter


project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from utils.r_wr_funcs import read_txt, save_txt


def frequency(input_file: str, output_file: str) -> None:
    """
    Count frequency for each letter in input file

    Args:
    input_file: the source text file
    outpute_file: ready-made frequency analysis
    """
    s = read_txt(input_file)

    c = Counter(s)
    l = len(s)
    
    res = ""
    for key, val in c.most_common():
        res += f"{key}: {round(val/l, 5)}\n"
    save_txt(output_file, res)
    

def main() -> None:
    """
    Uses argparse to process command-line arguments
    and calls the frequency() function to to calculate the frequency analysis.
    """
    parser = argparse.ArgumentParser(description = frequency.__doc__)
    parser.add_argument("input_file", type = str, help = "Input file name")
    parser.add_argument("output_file", type = str, help = "Output file name")

    args = parser.parse_args()
    
    frequency(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
    #python utils\frequency.py task_2\origin.txt task_2\frequency.txt