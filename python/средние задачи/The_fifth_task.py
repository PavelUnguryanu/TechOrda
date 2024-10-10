# Напишите программу для нахождения всех совершенных чисел (чисел, равных сумме своих делителей, исключая само число) в заданном диапазоне. Диапазон от 0 до 1000

def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

for number in range(1, 1001):
    if is_perfect(number):
        print(number)