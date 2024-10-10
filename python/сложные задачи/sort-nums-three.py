# #sort-nums-three 
# Напишите функцию, которая отсортировывает по возрастанию три числа a, b, c, без использования циклов.
# Отсортированные числа вывести в консоль.
# Пример
# 3 2 1 -> 1 2 3
# Sample Input:
# 3 2 1
# Sample Output:
# 1 2 3

def sort_nums_three(a, b, c):
    
    min_num = min(a, b, c)
    max_num = max(a, b, c)
    
    total_sum = a + b + c
    
    mid_num = total_sum - min_num - max_num
    
    print(min_num, mid_num, max_num)


sample_input = input("Введите три числа через пробел: ")
a, b, c = map(int, sample_input.split())
sort_nums_three(a, b, c)