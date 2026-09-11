import sys

def split_character(s: str) -> None:
    for i in range(0, len(s), 8):
        print(s[i:i + 8].ljust(8, "0"))


for line in sys.stdin:
    split_character(line.strip())