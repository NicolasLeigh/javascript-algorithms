def prime_factors(num: int) -> str:
    factors = []

    i = 2
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i

        i += 1

    if num > 1:
        factors.append(num)

    return " ".join(map(str, factors))


num = int(input().strip())
print(prime_factors(num))