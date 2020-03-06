def to_rna(dna_strand):
    arn = dna_strand.translate("".maketrans("CGTA", "GCAU"))
    return arn
