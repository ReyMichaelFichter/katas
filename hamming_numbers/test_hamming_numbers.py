from .hamming_numbers import hamming


def test_hamming():
    assert hamming(1) == 1
    assert hamming(2) == 2
    assert hamming(10) == 12
    assert hamming(15) == 24
    assert hamming(150) == 5832