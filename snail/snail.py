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
    if not matrix[0]:
        return []
    out = []
    start = 0
    end = len(matrix) - 1
    while end - start > 0:
        out.extend([x for x in matrix[start][start:end]])
        out.extend([x for x in list(zip(*matrix))[end][start:end]])
        out.extend([x for x in list(reversed(matrix[end]))[start:end]])
        out.extend(
            [x for x in list(reversed(list(zip(*matrix))[start]))[start:end]]
        )
        start += 1
        end -= 1
    if start == end:
        out.append(matrix[start][end])
    return out
