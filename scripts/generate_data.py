import numpy as np

RNG = np.random.default_rng()
NUCLEOTIDES = ["A", "T", "G", "C"]


def generate_primers(
    filename: str = "data/primers.fasta",
    n_primers: int = 10,
    min_primer_length: int = 10,
    max_primer_length: int = 50,
) -> str:
    """
    Generates random primers for analysis.
    :param n_primers:
    :param min_primer_length:
    :param max_primer_length:
    :param filename:
    :return: path to output file
    """
    primer_range = range(1, n_primers + 1)

    with open(filename, "w") as file:
        for primer_number in primer_range:
            for primer_subnumber in primer_range:
                primer_length = RNG.integers(
                    low=min_primer_length, high=max_primer_length
                )
                primer_F_seq = "".join(np.random.choice(NUCLEOTIDES, primer_length))
                primer_R_seq = "".join(np.random.choice(NUCLEOTIDES, primer_length))
                file.write(
                    f">loc_{primer_number}.{primer_subnumber}_F\n"
                    f"{primer_F_seq}\n"
                    f">loc_{primer_number}.{primer_subnumber}_R\n"
                    f"{primer_R_seq}\n"
                )

    return filename


def generate_genes(
    filename: str = "data/genes.fasta",
    n_genes: int = 10,
    min_gene_size: int = 100,
    max_gene_size: int = 340,
    line_size_in_fasta: int = 70,
) -> str:
    """
    Generates random genes for analysis.
    :param n_genes:
    :param min_gene_size:
    :param max_gene_size:
    :param line_size_in_fasta:
    :param filename:
    :return: path to output file
    """
    gene_range = range(1, n_genes + 1)  # number of genes

    with open(filename, "w") as file:
        for gene_number in gene_range:
            gene_length = RNG.integers(low=min_gene_size, high=max_gene_size)
            gene_lines = gene_length // line_size_in_fasta

            file.write(f">loc_{gene_number}\n")
            for gene_line in range(gene_lines):
                gene_seq = "".join(np.random.choice(NUCLEOTIDES, line_size_in_fasta))
                file.write(f"{gene_seq}\n")

            remain_gene_length = gene_length - gene_lines * line_size_in_fasta
            if remain_gene_length != 0:
                remain_gene_seq = "".join(
                    np.random.choice(NUCLEOTIDES, remain_gene_length)
                )
                file.write(f"{remain_gene_seq}\n")

    return filename
