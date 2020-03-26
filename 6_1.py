d, m, y = int(input('day: ')), int(input('month: ')), int(input('year: ')) # користувач вводить дату: день, місяць, рік
# в стрічках 8-11 ми вказуємо в якому діапазоні мають знаходитись ці значення
days = range(1, 32) 
months = range(1, 13)
years = range(1901, 2021)
years_sp = range(1904, 2021, 4)
# в двох наступних if перевіряємо чи рік і місяць в потрібному діапазоні
if y in years: 
    if m in months:
        if m in range(1, 8, 2) or m in range(8, 13, 2): # обираємо місяці, в яких 31 день
            if d in range(1, 32): # чи день в потрібному діапазоні
                if m == 1 and d == 1: # враховуємо можливість переходу на попередній рік 
                    # в рядках 19-73 прораховуємо всі можливі комбінації дня, місяця і року
                    # присвоюючи після перевірки який місяць і день змінним значення попереднього і наступного
                    ld, lm, ly, nd, nm, ny = 31, 12, y - 1, d + 1, m, y
                elif m == 3 and d == 1:
                    if y in years_sp:
                        ld, lm, ly, nd, nm, ny = 29, m - 1, y, d + 1, m, y
                    else:
                        ld, lm, ly, nd, nm, ny = 28, m - 1, y, d + 1, m, y
                elif m == 12 and d == 31:
                    ld, lm, ly, nd, nm, ny = d - 1, m, y, 1, 1, y + 1
                elif m == 8 and d == 1:
                    ld, lm, ly, nd, nm, ny = 31, m - 1, y, d + 1, m, y
                elif d == 1:
                    ld, lm, ly, nd, nm, ny = 30, m - 1, y, d + 1, m, y
                elif d == 31:
                    ld, lm, ly, nd, nm, ny = d - 1, m, y, 1, m + 1, y
                else:
                    ld, lm, ly, nd, nm, ny = d - 1, m, y, d + 1, m, y
                print(f'The last day is {ld}.{lm}.{ly}.', f'The next day is {nd}.{nm}.{ny}', sep='\n')
            else: # якщо дата не в заданному діапазоні, виводимо помилку
                print('There are only 31 days in this month.')
        elif m == 2: 
            if y in years_sp:
                if d in range(1, 30):
                    if d == 1:
                        ld, lm, ly, nd, nm, ny = 31, m - 1, y, d + 1, m, y
                    elif d == 29:
                        ld, lm, ly, nd, nm, ny = d - 1, m, y, 1, m + 1, y
                    else:
                        ld, lm, ly, nd, nm, ny = d - 1, m, y, d + 1, m, y
                    print(f'The last day is {ld}.{lm}.{ly}.', f'The next day is {nd}.{nm}.{ny}', sep='\n')
                else:
                    print(f'There are only 29 days in this month {y} year.')
            else:
                if d in range(1, 29):
                    if d == 1:
                        ld, lm, ly, nd, nm, ny = 31, m - 1, y, d + 1, m, y
                    elif d == 29:
                        ld, lm, ly, nd, nm, ny = d - 1, m, y, 1, m + 1, y
                    else:
                        ld, lm, ly, nd, nm, ny = d - 1, m, y, d + 1, m, y
                    print(f'The last day is {ld}.{lm}.{ly}.', f'The next day is {nd}.{nm}.{ny}', sep='\n')
                else:
                    print(f'There are only 28 days in this month {y} year.')
        else:
            if d in range(1, 31):
                if d == 1:
                    ld, lm, ly, nd, nm, ny = 31, m - 1, y, d + 1, m, y
                elif d == 30:
                    ld, lm, ly, nd, nm, ny = d - 1, m, y, 1, m + 1, y
                else:
                    ld, lm, ly, nd, nm, ny = d - 1, m, y, d + 1, m, y
                print(f'The last day is {ld}.{lm}.{ly}.'
                      f'The next day is {nd}.{nm}.{ny}')
            else:
                print('There are only 30 days in this month.')
    else: # якщо місяці не в діапазоні, сповіщуєм користувача
        print('There are only 12 month')
else: # якщо всі складові дати не в діапазоні, друкуємо помилку
    print('Error')
