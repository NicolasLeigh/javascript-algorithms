def radix_change(hex_string: str) -> int:
    return int(hex_string, 16)


hex_string = input().strip()
print(radix_change(hex_string))