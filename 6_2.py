from enum import Enum # імпортуємо Enum для створення перелічень


class Converter(Enum): # створюємо клас Конвертер для валют USD, EUR, CZK i PLN
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


x = float(input('Amount of money: ')) # вводимо сумму
p = Converter[input('Input currency: ')] # обираємо валюту з класа Конвертер
# за допомогою if i elif перевіряємо, яку валюту обрав користувач
# і відповідно до обраного варіанту множимо на потрібне значення для отримання переведенної валюти
if p.value == 1:
    x *= 24.52
    print(x)
elif p.value == 2:
    x *= 26.75
    print(x)
elif p.value == 3:
    x *= 1.08
    print(x)
else:
    x *= 6.29
    print(x)
