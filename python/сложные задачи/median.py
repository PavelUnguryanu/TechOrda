# #median 
# Реализовать функцию median, которое находится в середине массива, если его упорядочить по возрастанию, то есть такое число, что половина из элементов набора не меньше него, а другая половина не больше.
# Если кол-во элементов в массиве четное, то нужно вернуть левое значение медианы.
# Ограничения
# 0 <= array.length <= 10_000
# Sample Input:
# [1, 2, 3]
# Sample Output:
# 2

def median(arr):

    arr.sort()
    n = len(arr)
    
    if n % 2 == 0:
        return arr[n // 2 - 1]
    
    else:
        return arr[n // 2]

try:
    input_str = input("Введите элементы массива через пробел: ")
    input_arr = list(map(int, input_str.split()))
    result = median(input_arr)
    print(f"Медиана: {result}")
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целые числа через пробел.")