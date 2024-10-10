# Реализуйте программу, которая определяет, является ли заданная дата корректной (). Выведите соответствующее сообщение.
# Дата дана в формате “20.01.2002”

from datetime import datetime

date_input = input("Введите дату в формате дд.мм.гггг: ")

try:
    date_obj = datetime.strptime(date_input, "%d.%m.%Y")
    print("Дата корректна.")
except ValueError:
    print("Дата некорретна.")