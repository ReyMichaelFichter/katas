import itertools

"""
The idea behind this algorithm:

let X be the sequence of all hamming numbers
    ( X = 1, 2, 3, 4, 5, 6, 8 ... )

This sequence can be divided into three subsequences X2, X3, X5 where 
Xi = X * i (elementwise multiplication), i.e
    X2 = [1*2, 2*2, 3*2, 4*2, 5*2, 6*2, 8*2, ...] = [2, 4, 6, 8, 10, 12, 16...]
    X3 = [1*3, 2*3, 3*3, 4*3, 5*3, 6*3, 8*3, ...] = [3, 6, 9, 12, 15, 18, 24...]
    X5 = [1*5, 2*5, 3*5, 4*5, 5*5, 6*5, 8*5, ...] = [5, 10 15, 20, 25, 30, 40...]

It can be shown that Union(X2, X3, X5, 1) = X


For each subsequence:
    generate the next number
While True:
    The smallest of is the next hamming number.
    For the subsequence(s) that contained the next hamming number:
        generate the next number.

"""


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
