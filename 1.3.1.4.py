import numpy as np  # імпортуємо numpy

a = np.ones((4, 4), dtype=int)  # заповнюємо массив функцією ones()
for i in range(4):
    for j in range(4):
        a[i, j] = int(input(f'Input [{i + 1}][{j + 1}] element: '))  # користувач вводить елементи почергово
        if a[i, j] < 0:  # порівнюємо значення кожного елемента з нулем
            a[i, j] = 0  # присвоюємо від*ємним елементам значення 0
print(a)