import pytest

from anagrams import make_anagrams, is_anagram


@pytest.mark.parametrize(
    "words, expected",
    [
        (["kinship", "pinkish"], [("kinship", "pinkish")]),
        (
            ["kinship", "enlist", "inlets", "pinkish", "listen", "silent"],
            [("kinship", "pinkish"), ("enlist", "inlets", "listen", "silent")],
        ),
        (
            [
                "crepitus",
                "cuprites",
                "pictures",
                "piecrust",
                "paste",
                "pates",
                "peats",
                "septa",
                "spate",
                "tapes",
                "tepas",
                "punctilio",
                "unpolitic",
                "sunders",
                "undress",
            ],
            [
                ("crepitus", "cuprites", "pictures", "piecrust"),
                ("paste", "pates", "peats", "septa", "spate", "tapes", "tepas"),
                ("punctilio", "unpolitic"),
                ("sunders", "undress"),
            ],
        ),
    ],
)
def test_make_anagrams(words, expected):
    assert make_anagrams(words) == expected


@pytest.mark.parametrize(
    "word1, word2, expected",
    [("kinship", "pinkish", True), ("asdf", "hhhh", False)],
)
def test_is_anagram(word1, word2, expected):
    assert is_anagram(word1, word2) == expected
