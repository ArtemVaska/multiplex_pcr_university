from typing import Dict


def read_fasta(file_path: str) -> dict:
    sequences = {}
    current_id = None
    current_seq = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    sequences[current_id] = current_seq
                current_id = line[1:]
                current_seq = ""
            else:
                current_seq += line
        if current_id:
            sequences[current_id] = current_seq

    return sequences


def convert_multiline_fasta_to_oneline(
    input_fasta: str, output_fasta: str = None
) -> str:
    """
    Creates oneline fasta from multiline fasta.
    :param input_fasta: input filename
    :param output_fasta: output filename; <input_filename>_oneline.fasta if not provided
    :return: a dictionary with id of sequence and its sequence
    """
    seqs = {}
    with open(input_fasta) as multiline_fasta:
        seq = []
        for line in multiline_fasta:
            line = line.strip()
            if line.startswith(">"):
                if len(seq) != 0:
                    seqs[seq_id] = "".join(seq)
                    seq = []
                seq_id = line
            else:
                seq.extend(line)
        seqs[seq_id] = "".join(seq)

    if output_fasta is None:
        output_fasta = input_fasta.split(".")[0] + "_oneline.fasta"

    with open(output_fasta, mode="w") as oneline_fasta:
        for seq_id, seq in seqs.items():
            oneline_fasta.write(f"{seq_id}\n")
            oneline_fasta.write(f"{seq}\n")

    return output_fasta


def filter_primers(
    primers_parsed: dict, min_length: int = 15, max_length: int = 40
) -> dict:

    primers_valid = {}

    for primer_id, primer_seq in primers_parsed.items():
        if min_length <= len(primer_seq) <= max_length:
            primers_valid[primer_id] = primer_seq

    return primers_valid
