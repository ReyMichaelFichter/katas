def hamming(n):
    count = 1
    h = 1
    while count < n:
        h += 1
        while not is_hamming(h):
            h += 1
        count += 1
    return h


def maxDivide(n, d):
    while n % d == 0:
        n = n / d
    return n


def is_hamming(num):
    num = maxDivide(num, 2)
    num = maxDivide(num, 3)
    num = maxDivide(num, 5)
    return num == 1
