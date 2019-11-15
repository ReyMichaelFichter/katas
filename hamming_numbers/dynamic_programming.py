import itertools


def hamming_generator():
    # Initialize
    h = 1
    yield h
    _h = [h]  # Memoize the sequence hamming numbers
    bases = [2,3,5]
    expos = [0,0,0]
    multiples = [_h[expos[i]]*bases[i] for i in range(3)]
    while True:
        h = min(multiples)
        yield h
        _h.append(h)
        if h == multiples[0]:
            expos[0] += 1
            multiples[0] = _h[expos[0]] * bases[0]
        if h == multiples[1]:
            expos[1] += 1
            multiples[1] = _h[expos[1]] * bases[1]
        if h == multiples[2]:
            expos[2] += 1
            multiples[2] = _h[expos[2]] * bases[2]


def hamming(n):
    return list(itertools.islice(hamming_generator(), n))[-1]
