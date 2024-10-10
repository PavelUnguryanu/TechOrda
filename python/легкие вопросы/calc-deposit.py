def calc_deposite(n, k, b):
    for _ in range(n):
        b += b * (k / 100)
    return b
n, k, b = map(float, input("Введите  количество месяцев, процентную ставку и начальный баланс через пробел: ").split())
print(calc_deposite(int(n), k, b))