# Реализуйте программу для проверки, является ли заданное число числом Фибоначчи (число, которое является членом последовательности Фибоначчи). Заданное число 25

import math
def is_fibonacci(n):
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    return is_perfect_square(5 * n * n +4) or is_perfect_square(5 * n * n -4)
number = 25
if is_fibonacci(number):
    print(f"{number} является числом Фибоначчи.")
else:
    print(f"{number} не является числом Фибоначчи.")
