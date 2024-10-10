# #swap-bits 
# Реализуйте метод, который меняет местами первые 4 бита с остальными 4 и возвращает результат.
# Примеры
# 0000 1111 -> 1111 0000
# 0110 0111 -> 0111 0110
# Ограничения
# 0 <= a <= 255
# Sample Input:
# 15
# Sample Output:
# 240


def swap_bits():
    try:
        
        a = int(input("Введите число (от 0 до 255): "))
        if 0 <= a <= 255:
            
            lower_bits = a & 0b1111
            
            upper_bits = a >> 4

            result = (lower_bits << 4) | upper_bits
            print(result)
        else:
            print("Число должно быть в диапазоне от 0 до 255.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
swap_bits()