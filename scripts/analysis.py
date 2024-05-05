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
