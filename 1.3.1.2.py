import numpy as np  # імпортуємо numpy
import copy  # імпортуємо copy

a = np.ones((3, 3), dtype=int)  # використовуємо функцію ones() для заповнення массиву
for i in range(3):
    for j in range(3):
        a[i, j] = int(input(f'Input [{i + 1}][{j + 1}] element: '))  # користувач вводить елементи массиву

deep_copy = copy.deepcopy(a)  # змінній deep_copy присвоюється значення а

for i in range(3):
    for j in range(3):
        a[i, j] = deep_copy[j, i]  # присвоюємо нові значення кожному елементу з массиву а

print(a)