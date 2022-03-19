list_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
ls_idx = []  # собираю индексы чисел

for idx in list_data:
    count = list_data.index(idx)  # запоминает индекс по списку от нуля
    one_ls_data = list_data[count]  # разбиваю список на объекты
    one_ls = list(one_ls_data)  # разбиваю каждый объект на отдельный список

    for i in one_ls:
        formula = '0' <= i <= '9'  # формула поиска цифр, если формула нашла цифру, запускает цикл while
        control = True  # для запуска цикла
        while formula == control:  # пока условие истина, цикл выполняется
            sum = int(one_ls_data)  # полученное число перевожу к нужному типу
            control = False  # меняю значение для выхода из цикла
            if sum < 9 and one_ls[0] != '+':  # ищу первое число меньше 10 и которое не содержит +
                sum = '0' + str(sum)  # прибавляю к числу 0 и перевожу в строковое значение
                list_data[count] = sum  # заношу число в список по индексу
                ls_idx.append(count)  # добавляю индекс в новый список
            elif sum < 9 and one_ls[0] == '+':  # ищу второе число меньше 10 и которое содержит +
                sum = '+0' + str(sum)  # прибавляю к числу +0 и перевожу в строковое значение
                list_data[count] = sum  # заношу число в список по индексу
                ls_idx.append(count)
            elif sum > 9:  # ищу индекс 17
                ls_idx.append(count)

idx_rever = []  # пустой список для удаления дубликатов индекса
for rev in ls_idx:  # заношу каждое значение в rev
    if rev not in idx_rever:  # если в списке нет этого числа
        idx_rever.append(rev)  # добавить
        idx_rever.sort()  # отсортировать по порядку
        idx_rever.reverse()  # привести в обратный порядок

for x in idx_rever:  # в обратном порядке добавляю знаки
    list_data.insert(x + 1, '"')  # сначала после индекса
    list_data.insert(x, '"')  # потом перед индексом

message = ''  # пустая строка
for item in list_data:  # помещаю список в переменную
    quotes = '"'
    plus = '+'
    pl_item = plus in item  # проверяю, есть ли плюс в переменной
    if item == quotes:  # если это кавычка убираю пробелы
        message += ''
        message += item
        message += ''
    elif item > '0' and item < '9' or pl_item == True:  # если это цифра или содержит плюс, вставлять как есть
        message += item
        continue
    else:  # все остальные случаи отступить
        message += ' '
        message += item
        message += ' '

print(list_data)
print(message)
