def custom_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
user_input = input("Введите числа, разделеные пробелом: ")
array = list(map(int, user_input.split()))
print("Сумма чисел:", custom_sum(array))