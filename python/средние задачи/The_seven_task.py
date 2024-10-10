# Напишите программу, которая определяет, является ли заданное число совершенным числом (число, равное сумме своих делителей, исключая само число). Выведите сообщение с результатом.

def is_perfect(num):
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num
number = int(input("Введите число: "))
if is_perfect(number):
    print(f"{number} является совершенным числом.")
else:
    print(f"{number} не является совершенным числом.")
    