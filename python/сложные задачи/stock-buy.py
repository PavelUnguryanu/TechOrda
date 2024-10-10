# #stock-buy 
# Два друга хотят скинуться, чтобы купить акции на Jusan Invest. Им нужно купить две акции на всю сумму, которая у них есть.
# Дается доступная сумма денег m и список цен на различные акции s. Напечатайте индексы акции, которые можно купить.
# Напечатанные индексы должны быть отсортированы по возрастанию.
# Предполагается, что такие числа всегда существуют в списке цен акции s, сумма которых равна m.
# Пример
# m = 8, s = [8 7 3 1 3 10]
# Правильный ответ
# 1 3
# Число по индексу [1] это 7, а по индексу [3] это 1. Соответственно, 7 + 1 = 8.
# Ограничения
# m > 1
# 2 <= array.length <= 10_000
# Sample Input:
# 3
# [1, 2, 3]
# Sample Output:
# 0 1

def find_stock_indices(m, s):

    price_to_index = {}
    for i, price in enumerate(s):
        complement = m - price
        if complement in price_to_index:
            return sorted([price_to_index[complement], i])
        price_to_index[price] = i
    return None
try:
    m = int(input("Введите доступную сумму денег: "))
    input_str = input("Введите цены на акции через пробел: ")
    input_arr = list(map(int, input_str.split()))
    result = find_stock_indices(m, input_arr)
    if result:
        print(*result)
   
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целые числа.")