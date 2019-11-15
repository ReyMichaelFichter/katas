import itertools


def hamming_generator():
    # Initialize
    h = 1
    yield h
    _h = [h]  # Memoize the sequence hamming numbers
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    multiples = [_h[expos[i]] * bases[i] for i in range(3)]
    while True:
        h = min(multiples)
        yield h
        _h.append(h)
        for i in range(3):
            expos[i] += int(h == multiples[i])

def hamming(n):
    return list(itertools.islice(hamming_generator(), n))[-1]
