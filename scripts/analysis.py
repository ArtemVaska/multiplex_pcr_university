COMPLEMENT_TABLE = {"A": "T", "T": "A", "G": "C", "C": "G"}


def complement(seq: str) -> str:
    complement_seq = []
    for nucleotide in seq:
        complement_seq.extend(COMPLEMENT_TABLE[nucleotide])
    complement_seq = "".join(complement_seq)
    return complement_seq


def find_primer_dimers(primers_valid: dict, window_size: int = 5) -> list:

    primers_list = []
    for id, seq in primers_valid.items():
        primers_list.append([id, seq])

    dimers = []

    for query_n_id, query_primer in enumerate(primers_list):
        query_id, query_seq = primers_list[query_n_id]
        for subject_primer in primers_list[query_n_id + 1 :]:
            subject_id, subject_seq = subject_primer
            check_next = True

            for query_iteration in range(len(query_seq) - window_size + 1):
                if not check_next:
                    break
                query_iteration_subset_seq = query_seq[
                    query_iteration : query_iteration + window_size
                ]
                for subject_iteration in range(len(subject_seq) - window_size + 1):
                    subject_iteration_subset_seq = subject_seq[
                        subject_iteration : subject_iteration + window_size
                    ]
                    if query_iteration_subset_seq == complement(
                        subject_iteration_subset_seq
                    ):
                        dimers.append([query_id, subject_id])
                        check_next = False
                        break

    return dimers
    
def parse_primers(
    gene_id: str,
    primers_valid: dict
) -> dict:  # находит в словаре primers_valid праймеры для одного гена
    gene_id = gene_id + '_'
    regex = fr"\b{gene_id}\b"

    primer_one_loci = {}

    for primer_id, primer_seq in primers_valid.items():
      if re.findall(regex, primer_id):
        primer_one_loci[primer_id] = primer_seq

    return primer_one_loci


def align(gene_seq, primer_seq) -> float:
    aligner = Align.PairwiseAligner()
    score = aligner.score(seq, primer)
    return score


def get_alignment_scores(genes: dict, primers: dict) -> dict:

    alignment_scores = {}

    for gene_id, gene_seq in genes.items():
        gene_id_primers = parse_primers(gene_id, primers)

        for primer_id, primer_seq in gene_id_primers.items():
        	if re.search('R', primer_id) is not None:
        	gene_seq = reversed(gene_seq)
        	gene_id_alignment_score = align(gene_seq, primer_seq)
            # if primer_id in gene_id_dimers:
            #     is_dimer = True
            # else:
            #     is_dimer = False
            alignment_scores[gene_id] = {primer_id: gene_id_alignment_score}

    return alignment_scores


def find_best_primer(alignment_scores: dict) -> str:

    for gene_id, primer_id in alignment_scores.items():
        max_primer_score_F = 0
        max_primer_score_R = 0
        gene_id_dimers = find_primer_dimers(alignment_scores[gene_id], window_size=5)

        # сравниваем и учитываем, чтобы не было элемента в gene_id_dimers [primer_F, primer_R] или [primer_R, primer_F]


alignment_scores = get_alignment_scores(genes, primers)
best_primers = find_best_primer(alignment_scores)
