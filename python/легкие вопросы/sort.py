def selection_sort(arr):

    n = len(arr)
    
    for i in range(n):
    
        min_index = i
    
        for j in range(i + 1, n):
    
            if arr[j] < arr[min_index]:
    
                min_index = j
    
        arr[i], arr[min_index] = arr[min_index], arr[i]

user_input = input("Введите числа, разделенные пробеломи: ")

array = list(map(int, user_input.split()))

selection_sort(array)

print("Отсортированный массив:", array)
