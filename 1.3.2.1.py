a = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'] #пространство поиска

#функция поиска
def linear_search_3(lst, x):
    pos = 0 #начальная позиция
    while lst[pos] != x: #если элемент в текущей позиции не равен искомому
        pos += 1 #продолжаем, увеличивая номер позиции на 1
    return pos + 1 #возврвщаем pos + 1 т.к. индексация идёт с 0

print("serching space : ", a)
print("enter value to search number : ")
x = input()
print(x, "index is", linear_search_3(a, x))
