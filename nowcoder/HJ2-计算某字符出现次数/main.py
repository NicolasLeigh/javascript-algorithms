def count_char1(s: str, char: str) -> int:
    chars = s.strip().lower()
    count = {}

    for c in chars:
        count[c] = count.get(c, 0) + 1

    return count.get(char.lower(), 0)

# Solution 2
from collections import Counter

def count_char(s: str, char: str) -> int:
    count = Counter(s.strip().lower())
    return count.get(char.lower(), 0)

a = input()
b = input()
print(count_char(a, b))