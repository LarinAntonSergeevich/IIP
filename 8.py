def binary_to_decimal(binary: str) -> int:
    decimal = 0
    for i, ch in enumerate(binary[::-1]):
        decimal += int(ch) * (2 ** i)
    return decimal
