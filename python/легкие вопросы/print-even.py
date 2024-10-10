def print_even_a_b(a, b):
    if a % 2 != 0:
        a += 1
    for i in range(a, b + 1, 2):
        print(i, end=" ")
a, b = map(int, input("Введите два числа через пробел:").split())

print_even_a_b(a, b)
