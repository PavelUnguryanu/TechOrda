# #переменная
# ##sum-1-n 
# Дается число n. Вернуть сумму от 1 до n без использования циклов.
# Ограничения
# 1 <= n <= 65535
# Sample Input:
# 5
# Sample Output:
# 15


def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

# Пример использования:
n = int(input("Введите число n: "))
if n < 1 or n > 65535:
    print("Так нельзя")
else:
    print(sum_recursive(n))