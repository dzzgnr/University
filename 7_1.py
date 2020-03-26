'''
а) Дана послідовність цілих чисел а1, ..., аn. Для кожного з чисел, що входять в
послідовність а1, ..., аn з'ясувати, скільки разів воно входить в цю послідовність.
Результат представити у вигляді ряду рядків, перший з яких є а1 - k, де k - число входжень
а1 в послідовність а1, ..., аn. Другий рядок буде мати вигляд аj - m, де аj - перший по
порядку член послідовності, відмінний від а1, а m - число входжень цього члена в
послідовність.
Бондаренко Даниїл
'''
from random import randint  # імпортуємо randint для заповнення порожньої послідовності числами

n = int(input('Введіть довжину послідовності: '))  # користувач задає довжину послідовності
a = [randint(0, 7) for i in range(n)]  # заповнює її функція randint
b = []  # створюємо порожній список, щоб потім додавати в нього елементи
print(a)
for k in a:
    g = a.count(k)  # фкнція count дя кожного елемента рахує скільки раз він зустрічався
    if k not in b:  # щоб значення у списку b не повторювались, ставимо саме таку умову
        b.append(k)  # додаємо в b елемент k
    else:
        continue
    print(k, '-', g)  # виводимо елемент і його кількість у списку а
