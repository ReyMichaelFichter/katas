import time
from collections import defaultdict
from typing import List, Tuple


def make_anagrams(words: List[str]) -> List[Tuple[str, ...]]:
    anas = defaultdict(list)
    for x in words:
        anas[hash("".join(sorted(x)))].append(x)
    return [tuple(val) for val in anas.values()]


def is_anagram(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    if sorted(word1) != sorted(word2):
        return False
    return True


if __name__ == "__main__":
    with open("words.txt", "r") as f:
        words = f.readlines()
    t0 = time.time()
    make_anagrams(words)
    t1 = time.time()
    print(f"It took {t1-t0} seconds to make all anagrams")
