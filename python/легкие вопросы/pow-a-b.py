def pow_a_b(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result
a, b = map(int, input("Введите значения через пробел:").split())
print(pow_a_b(a, b))