import pytest

from python.string_calculator import StringCalculator


def test_string_calculator():
    assert StringCalculator().add("") == 0
    assert StringCalculator().add() == 0
    assert StringCalculator().add("1") == 1
    assert StringCalculator().add("1,2") == 3
    assert StringCalculator().add("1\n2") == 3
    assert StringCalculator().add("1\n3,2") == 6


def test_pass_in_delimiter():
    assert StringCalculator().add("//;\n1;2") == 3
    assert StringCalculator().add("///\n1/2\n7/1") == 11


def test_extract_delimiter():
    assert StringCalculator().extract_delimiter("//;\n1;2") == (";", "1;2")
    assert StringCalculator().extract_delimiter("//;\n1;2\n3;4") == (
        ";",
        "1;2;3;4",
    )
    assert StringCalculator().extract_delimiter("///\n1/2\n7/1") == (
        "/",
        "1/2/7/1",
    )


def test_no_negative_numbers():
    with pytest.raises(ValueError) as e:
        StringCalculator().add("1,2\n-4,3")
