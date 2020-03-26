"""б) Задача. Визначити кількість товарів, які продані менш ніж рік тому і вивести
відомості про них. Поля структури: Продавець, Найменування товару, Кількість, Ціна,
Дата продажу.
Бондаренко Даниїл"""
# в строках 6-9 ініціалізуємо словник значеннями продавець, продукт, кількість, ціна, дата продажу
products = [{'seller': 'Boris', 'product_name': 'bread', 'count': 2, 'cost': 1, 'date_of_sale': 2019},
            {'seller': 'Petro', 'product_name': 'bread', 'count': 5, 'cost': 1, 'date_of_sale': 1941},
            {'seller': 'Sergiy', 'product_name': 'bread', 'count': 3, 'cost': 1, 'date_of_sale': 1488},
            ]

count_of_products_type = len(products)  # рахуємо скільки товару є взагалі
elements = []  # створюємо порожній список, щоб потім заносити у нього значення
all_count = 0  # змінна, у якій буде зберігатись кінцевий результат
for i in range(0, len(products)):
    date = products[i].get('date_of_sale')  # для кожного продукту знаходимо дату продажу функцією get
    if 2020 - date <= 1:  # порівнюємо дату з теперішнім роком
        all_count += products[i].get('count')  # додаємо в змінну з кінцевим результатом кількість певної одиниці товару
        elements.append(i)  # в список додаємо номер елемента, який підходить за описом
for i in elements:
    print(f'products by the desired date: {products[i]}')  # для потрібного товару виводимо, що це за товар
print(f'count of all products by the desired date: {all_count}')  # виводимо кількість його одиниць
