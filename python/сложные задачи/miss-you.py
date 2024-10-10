# #miss-you 
# Дается два массива чисел, вернуть числа из второго массива, которые не присутствуют в первом в отсортированном порядке.
# Ограничения
# 0 <= array1.length <= 10_000
# 0 <= array2.length <= 10_000
# Sample Input:
# [1, 1, 3, 2, 5]
# [1, 3, 9, 1, 5, 7]
# Sample Output:
# [7, 9]


def find_missing_numbers(array1, array2):

    set1 = set(array1)
    set2 = set(array2)
    
    missing_numbers = sorted(set2 - set1)
    return missing_numbers
try:
    input_str1 = input("Введите элементы первого массива через пробел: ")
    input_arr1 = list(map(int, input_str1.split()))
    input_str2 = input("Введите элементы второго массива через пробел: ")
    input_arr2 = list(map(int, input_str2.split()))
    result = find_missing_numbers(input_arr1, input_arr2)
    print(result)
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целые числа через пробел.")