import itertools


def hamming_generator():
    # Initialize
    h = 1
    yield h
    _h = [h]  # Memoize the sequence hamming numbers
    bases = [2,3,5]
    expos = [0,0,0]
    next_multiple_of_2 = _h[expos[0]] * bases[0]
    next_multiple_of_3 = _h[expos[1]] * bases[1]
    next_multiple_of_5 = _h[expos[2]] * bases[2]
    while True:
        h = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        yield h
        _h.append(h)
        if h == next_multiple_of_2:
            expos[0] += 1
            next_multiple_of_2 = _h[expos[0]] * bases[0]
        if h == next_multiple_of_3:
            expos[1] += 1
            next_multiple_of_3 = _h[expos[1]] * bases[1]
        if h == next_multiple_of_5:
            expos[2] += 1
            next_multiple_of_5 = _h[expos[2]] * bases[2]


def hamming(n):
    return list(itertools.islice(hamming_generator(), n))[-1]
