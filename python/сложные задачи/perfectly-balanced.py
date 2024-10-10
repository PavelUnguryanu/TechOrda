# #perfectly-balanced 
# Дается массив чисел, найти в массиве такой элемент, где сумма чисел слева равна сумме чисел справа.
# Если такое число есть, то вернуть true, в противном случае false.
# Пример
# Возьмем массив 1, 2, 9, 8, 5, 7
# Число 8 является элементом, где сумма чисел слева равна сумме чисел справа.
# 1   2   9   8   5   7

# (1+2+9)=12  ↑  (5+7)=12
# Ограничения
# 0 <= array.length <= 10_000
# Sample Input:
# [1, 2, 9, 8, 5, 7]
# Sample Output:
# true

def find_perfectly_balanced_element(arr):
    total_sum = sum(arr)
    left_sum = 0
    for num in arr:
        total_sum -= num
        if left_sum == total_sum:
            return True
        left_sum += num
    return False
try:
    input_str = input("Введите элементы массива через пробел: ")
    input_arr = list(map(int, input_str.split()))
    result = find_perfectly_balanced_element(input_arr)
    print(result)
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целые числа через пробел.")