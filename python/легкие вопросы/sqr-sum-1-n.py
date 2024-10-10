def sqrKvadro(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i*i

    return sum

n = int(input("Введите значение n: "))
if n < 1 or n > 10860:
    print("Так нельзя")
else:
    print(sqrKvadro(n))