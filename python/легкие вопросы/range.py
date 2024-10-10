def custom_range(n):
    arr = [i for i in range(1, n + 1)]
    return arr
n = int(input("Введите число: "))
arr = custom_range(n)
for i in range(len(arr)):
    print(arr[i], end = " ")