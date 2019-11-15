import itertools


def hamming_generator():
    # Initialize
    h = 1
    yield h
    _h = [h]  # Memoize the sequence hamming numbers
    i = j = k = 0
    next_multiple_of_2 = _h[i] * 2
    next_multiple_of_3 = _h[j] * 3
    next_multiple_of_5 = _h[k] * 5
    while True:
        h = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        yield h
        _h.append(h)
        if h == next_multiple_of_2:
            i += 1
            next_multiple_of_2 = _h[i] * 2
        if h == next_multiple_of_3:
            j += 1
            next_multiple_of_3 = _h[j] * 3
        if h == next_multiple_of_5:
            k += 1
            next_multiple_of_5 = _h[k] * 5


def hamming(n):
    return list(itertools.islice(hamming_generator(), n))[-1]
