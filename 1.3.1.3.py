import random
import numpy as np

def mult(m, n):
    sum = 0 #сумма
    temp = [] #временная матрица
    res = [] #конечная матрица
    if len(m) != len(n[0]): #проверка возможности умножения
        print("cant be multiplied")
    else:
        rows_1 = len(m) #количество строк в 1 матрице
        cols_1 = len(m[0]) #количество столбцов в 1 матрице
        rows_2 = cols_1 #количество строк во 2 матриц
        cols_2 = len(n[0]) #количество столбцов во 2 матрице

        #алгоритм умножения матриц, который мы выполняем, умножая матрицы вручную
        #идём по строкам первой и по столбцам второй, перемножаем элементы, суммируем 
        #каждое произведение и записываем результат в новую
        for i in range(0, rows_1):
            for j in range(0, cols_2):
                for k in range(0, cols_1):
                   sum += m[i][k] * n[k][j]
                temp.append(sum)
                sum = 0
            res.append(temp)
            temp = []
    return res

#функция которая создаёт матрицу 3х3 со случайными значениями
def creatematrix():
    t = [] #временная строка
    m = [] #результат
    for i in range(3):
        for j in range(3):
            t.append(random.randint(1, 10)) #создаём строку
        m.append(t) #добавляем в матрицу
        t = [] #обнуляем строку
    return m 

a = creatematrix()
b = creatematrix()
c = mult(a, b)
print("a :", a, "\n")
print("b :", b, "\n")
print("c = a * b :", c, "\n")
