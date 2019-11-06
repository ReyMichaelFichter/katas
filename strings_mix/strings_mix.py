from collections import defaultdict
from typing import List


def mix(s1: str, s2: str) -> str:
    l1, l2 = count_letters(s1), count_letters(s2)
    return assemble_str(l1, l2)


def count_letters(s: str) -> List[str]:
    d = defaultdict(str)
    for l in s:
        if l.islower():
            d[l] += l
    return [v for v in d.values() if len(v) > 1]


def assemble_str(l1: List[str], l2: List[str]) -> str:
    longest = []
    for x in l1:
        # if only in l1!
        if x[0] not in "".join(l2):
            longest.append(f"1:{x}")
        else:
            for y in l2:
                if x[0] == y[0]:  # Same letter
                    if len(x) > len(y):
                        longest.append(f"1:{x}")
                    elif len(x) < len(y):
                        longest.append(f"2:{y}")
                    else:
                        longest.append(f"=:{x}")
    for y in l2:
        if y[0] not in "".join(l1):
            longest.append(f"2:{y}")

    longest.sort(key=lambda w: (-len(w), ord(w[0]), ord(w[-1])))
    return "/".join(longest)
