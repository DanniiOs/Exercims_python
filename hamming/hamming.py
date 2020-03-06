def distance(strand_a, strand_b):
    cont = 0
    if len(strand_a) == len(strand_b):
        for distancia in range(len(strand_a)):
            if strand_a[distancia] != strand_b[distancia]:
                cont += 1
        return cont
    else:
        raise ValueError(strand_a, strand_b)
