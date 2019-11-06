import pytest

from strings_mix.strings_mix import mix, count_letters, assemble_str


@pytest.mark.parametrize(
    "s1, s2, res",
    [
        (
            "my&friend&Paul has heavy hats! &",
            "my friend John has many many friends &",
            "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss",
        )
    ],
)
def test_mix(s1, s2, res):
    assert mix(s1, s2) == res


@pytest.mark.parametrize("s, d", [("aaabbc", ["aaa", "bb"])])
def test_count_letters(s, d):
    assert count_letters(s) == d


@pytest.mark.parametrize(
    "l1, l2, res",
    [
        (["aaaa"], ["aaaaaa"], "2:aaaaaa"),
        (["aaaaaa"], ["aaa"], "1:aaaaaa"),
        (["aaa"], ["aaa"], "=:aaa"),
        (["aaa", "bbbb"], ["aaa"], "1:bbbb/=:aaa"),
        (["aaaa", "bbb"], ["ccc", "bbb"], "1:aaaa/2:ccc/=:bbb")
    ],
)
def test_assemble_str(l1, l2, res):
    assert assemble_str(l1, l2) == res
