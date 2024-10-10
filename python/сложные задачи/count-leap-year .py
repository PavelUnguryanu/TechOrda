# #count-leap-year  В этой задаче вам нужно вернуть кол-во високосных лет до заданного n года.
# Правило для определения високосного года [источник]: год, номер которого кратен 400, — високосный; 
# остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300); 
# остальные годы, номер которых кратен 
# 4, — високосные. все остальные годы — невисокосные. 
# Допускается, что високосные годы можно считать с 0 года. Пример До года 100 присутстует 24 високосных лет. 
# Ограничения n > 0 Запрещенные библиотеки, конструкции for 
# Sample Input: 
# 4 Sample Output: 1


def count_leap_year(n):
    # Подсчет високосных лет кратных 4, но не кратных 100
    # и добавление тех, что кратны 400
    return (n // 4) - (n // 100) + (n // 400)

# Ввод года от пользователя
n = int(input("Введите год: "))
if n <= 0:
    print("Год должен быть больше 0")
else:
    print(count_leap_year(n))
