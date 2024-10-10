# Создайте программу, которая определяет, в какой сезон года попадает заданная дата (месяц и день).
 
def determine_season(month, day):
    if (month == 12 and day >= 1) or (1 <= month <= 2) or (month == 3 and day <= 19):
        return "Зима"
    elif (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day <= 20):
        return "Весна"
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day <= 21):
        return "Лето"
    elif (month == 9 and day >= 22) or (10 <= month <= 11) or (month == 12 and day <= 20):
        return "Осень"

month = int(input("Введите номер месяца (1-12): "))
day = int(input("Введите день месяца: "))

season = determine_season(month, day)
print(f"Дата {day}.{month} попадает в сезон: {season}.")
