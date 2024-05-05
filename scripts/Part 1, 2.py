# Пункт 1: Cоздание FASTA файлов с придуманными последовательностями генов и праймеров
def write_fasta(file_path, sequences):
    with open(file_path, 'w') as file:
        for seq_id, seq in sequences.items():
            file.write(">" + seq_id + "\n")
            file.write(seq + "\n")

seqs = {
    "seq1": "ATGCGATCGTACTGATCGTACGAGTCGATCGAATGCGATCGTACTGATA",
    "seq2": "ATGCGATCGTACTATCGAATGC",
    "seq3": "ATCGATCGATCGATCG",
    "seq4": "ATGCGATCGTACTGATCGTACGAGTCGATCGAATGCGATCGTACTGATAGCTAGCTAGCTAGCTAGC",
    "seq5": "ATGCGATCGTACTATCGAATGCAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC",
    "seq6": "ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG",
    "seq7": "ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG",
    "seq8": "ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG"
}

primers = {
    "primer1.1_F": "ATCGAT",
    "primer1.1_R": "GATCGA",
    "primer1.2_F": "CGATCGATCGAT",
    "primer1.2_R": "CGATCG",
    "primer1.3_F": "ATCG",
    "primer1.3_R": "CGAT",
    "primer1.4_F": "CGATCGATCGATCGATC",
    "primer1.4_R": "GATCGATCGATCGATCG",
    "primer1.5_F": "CGATCGATCGATCGATCGAT",
    "primer1.5_R": "CGATCGATCGATCGATCGA",
    "primer1.6_F": "ATCGATCGATCGATCGATC",
    "primer1.6_R": "GATCGATCGATCGATCGAT",
    "primer1.7_F": "ATCGATCGATCGATCGATCG",
    "primer1.7_R": "CGATCGATCGATCGATCGA",
    "primer1.8_F": "ATCGATCGATCGATCGATCGAT",
    "primer1.8_R": "CGATCGATCGATCGATCGAT"
}

write_fasta("seqs.fasta", seqs)
write_fasta("primers.fasta", primers)

# Пункт 2: чтение FASTA файлов
def parse_fasta(file_path):
    sequences = {}
    current_id = None
    current_seq = ""
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = current_seq
                current_id = line[1:]
                current_seq = ""
            else:
                current_seq += line
        if current_id:
            sequences[current_id] = current_seq
    return sequences

seqs_parsed = parse_fasta("seqs.fasta")
primers_parsed = parse_fasta("primers.fasta")

# Пункт 3: отбор праймеров с длиной от 15 до 40
valid_primers = {}
for primer_id, primer_seq in primers_parsed.items():
    if 15 <= len(primer_seq) <= 40:
        valid_primers[primer_id] = primer_seq

print("Гены:")
print(seqs_parsed)
print("\nПраймеры:")
print(valid_primers)