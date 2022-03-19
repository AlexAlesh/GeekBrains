from copy import copy

rub = [95.15, 42, 65.2, 100.58, 52, 45.22, 67, 56.8, 120, 153.03, 0.7, 0.05]
print(id(rub))
comparison = (id(rub))

message = ''
for money in rub:
    if money == int(money):  # целые числа
        money_int = str(money)
        message += f'{money_int} руб 00 коп,'
    elif money == float(money):
        money_int_fl = money * 10 // 10  # получаю целое число
        int_fl = (money - money_int_fl) * 100 # получаю остаток
        sum = int(int_fl)
        if sum < 9:  # если остаток меньше 9 прибавляем 0
            message += f'{int(money_int_fl)} руб 0{sum} коп, '
        else:
            message += f'{int(money_int_fl)} руб {sum} коп, '

print('\n')
print(message)  # вывожу сообщение сколько рублей и копеек
print('\n')
rub.sort()  # сортировка по возрстанию
print('Сортировка по возрастанию:\n', rub, )
print(f'Изначальный список:  {comparison} \nОтсортированный список: {id(rub)}')
rub_copy = rub.copy()  # копия списка с другим id
print('Новый список с теми же ценами отсортированный по убыванию: ', id(rub_copy))
rub_copy.reverse()  # сортировка по убыванию
print(rub_copy)
# цены пяти самых дорогих товаров по возрастанию
rev = rub_copy[:5]
rev.sort()
print(rev)