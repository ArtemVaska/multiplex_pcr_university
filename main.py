from scripts.generate_data import generate_genes, generate_primers
from scripts.read_filter_data import (
    read_fasta,
    filter_primers,
    convert_multiline_fasta_to_oneline,
)


if __name__ == "__main__":
    # path_input = parse_args().input
    # path_output = parse_args().output
    path_genes = generate_genes("data/genes.fasta")
    path_primers = generate_primers("data/primers.fasta")
    print(f"Created fasta-files for analysis:\n" f"{path_genes}\n" f"{path_primers}\n")

    genes_oneline = convert_multiline_fasta_to_oneline(path_genes)
    primers_oneline = convert_multiline_fasta_to_oneline(path_primers)
    print(f"Created oneline fasta-files:\n" f"{genes_oneline}\n" f"{primers_oneline}\n")

    genes_parsed = read_fasta("data/genes.fasta")
    primers_parsed = read_fasta("data/primers.fasta")
    primers_valid = filter_primers(primers_parsed)
    print(
        f"Number of primers before filtration: {len(primers_parsed)}\n"
        f"Number of primers after filtration: {len(primers_valid)}\n"
    )
