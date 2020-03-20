import numpy as np #імпортуємо numpy як np

number_of_elements = int(input('Number of elements: ')) #користувач задає кількість елементів у массиві
array = np.ones(number_of_elements, dtype=int) #заповнюємо його за допомогою функції ones()
for i in range(number_of_elements):
    array[i] = int(input(f'Input {i + 1} element: ')) #вводимо почергово кожен елемент
print(array[::-1]) #використовуємо зріз, щоб відобразити масив в зворотньому порядку
