from random import randint

a = [] # создание списка
for i in range(15):
    a.append(randint(1, 50)) # заполнение его случайными значениями
a.sort() # сортировка

def binary_search(a, value):
    comp_count = 0
    mid = len(a) // 2 # индекс средины списка
    low = 0 # индекс начала списка
    high = len(a) - 1 # индекс конца списка
    # условие поиска :
    # пока центральный элементв не равен искомому и мы не добрались до конца списка
    while a[mid] != value and low <= high:
        comp_count += 2
        if value > a[mid]: # если искомое значение больше центрального
            comp_count += 1
            low = mid + 1 # искать будем в правой части списка
        else: # иначе в левой
            comp_count +=1
            high = mid - 1
            # и меняем индекс центра после перемещения влево
            mid = (low + high) // 2

    # если после всех переходов значени не найдено - выводим
    print("comparsion count =", comp_count)
    if low > high:
        print("no value")
    else: # если найдено - пишем его индекс
        print("index of", value, "is", mid + 1)

# искомое число
print(a)
print("enter value : ")
value = int(input())
binary_search(a, value)
