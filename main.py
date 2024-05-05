import argparse

from scripts.generate_data import generate_genes, generate_primers

# def parse_args():
#     parser = argparse.ArgumentParser(
#         usage="",
#         description="""""",
#     )
#     parser.add_argument("-i", "--input", nargs="?", help="")
#     parser.add_argument("-o", "--output", nargs="?", help="")
#
#     return parser.parse_args()
#
#


if __name__ == "__main__":
    # path_input = parse_args().input
    # path_output = parse_args().output
    path_genes = generate_genes()
    path_primers = generate_primers()
    print(f"Created files:\n" f"genes: {path_genes}\n" f"primers: {path_primers}\n")
