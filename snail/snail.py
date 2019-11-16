"""
    The snail problem.

    Given an NxN matrics of numbers, print the "snail sequence" of that matrix
    going around the matrix perimeter towards the matrix middle.
    e.g:

    snail(
            [[1,2,3],
            [4,5,6],
            [7,8,9]]
        )
        = [1,2,3,6,9,8,7,4,5]
"""


def snail(matrix):
    out = []
    while matrix:
        out.extend(matrix.pop(0))
        matrix = list(reversed(list(zip(*matrix))))
    return out
