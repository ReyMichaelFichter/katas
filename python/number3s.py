def find_all(sum_dig, digs):
    if digs == 1:
        return sum_dig if sum_dig < 10 else []

    if sum_dig == 0:
        return 0

    ans = 0

    for i in range(0, 10):
        if sum_dig-i >= 0:
            ans = str(ans) + str(find_all(sum_dig-i, digs-1))

    return int(ans)

