import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        usage="",
        description="""""",
    )
    parser.add_argument("-i", "--input", nargs="?", help="")
    parser.add_argument("-o", "--output", nargs="?", help="")

    return parser.parse_args()


if __name__ == "__main__":
    path_input = parse_args().input
    path_output = parse_args().output

