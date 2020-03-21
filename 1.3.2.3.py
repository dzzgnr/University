def string_search(x, s):
    state = 0 #индикатор того, нашли мы строку или нет
    for i in range(len(s) - len(x) + 1): #будем искать подстроку от начала строки до её конца - длина подстроки
        j = 0 #итератор подстроки
        while(j < len(x)): #пока не прошли всю подстроку
            if (s[i + j] != x[j]): #если один из символов не совпал
                break #продолжаем искать заново
            j += 1 #если совпал двигаем на следующий

        if (j == len(x)): #если в итоге количество совпадений = длине подстроки
            state = 1 #значит мы нашли её в строку
            print("substring founded at index", i)
    if state == 0: #если после прохода по строке подстрока не найдена
        print("substring does not exist")

string_search("qwerty", "fghfdhdfhqwerty")
