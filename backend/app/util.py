from typing import Dict
from collections import defaultdict


def count_letters(text: str) -> Dict[str, int]:
    result = defaultdict(int)
    for char in text.lower().replace(" ", ""):
        result[char] += 1
    return result
