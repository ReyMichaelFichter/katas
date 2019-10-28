import re
from typing import Tuple


class StringCalculator:
    def add(self, numbers: str = "") -> int:

        if not numbers:
            return 0
        if numbers.startswith("//"):
            delimiter, nums = self.extract_delimiter(numbers)
            numarr = [int(num) for num in nums.split(delimiter)]
            negatives = [num for num in numarr if num < 0]
            if negatives:
                raise ValueError("Negatives not allowed ", negatives[0])
            return sum([int(num) for num in nums.split(delimiter)])
        numarr = [int(num) for num in re.split(r"[,\n]", numbers)]
        negatives = [num for num in numarr if int(num) < 0]
        if negatives:
            raise ValueError("Negatives not allowed ", negatives[0])
        return sum(numarr)

    def extract_delimiter(self, numbers: str) -> Tuple[str, str]:
        lines = numbers.split("\n")
        delimiter = lines[0][2:]
        res = delimiter.join(lines[1:])
        return delimiter, res
