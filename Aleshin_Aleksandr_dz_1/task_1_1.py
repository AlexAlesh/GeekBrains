duration = int(input('Введите продолжительность: '))
#переменные:
days = duration // 86400
hours = duration // 3600 % 24
minutes = duration // 60 % 60
seconds = duration % 60
#вывод от переменных:
if days > 0:
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
elif hours > 0:
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
elif minutes > 0:
    print(minutes, 'мин', seconds, 'сек')
else:
    sec = seconds > 0
    print(seconds, 'сек')


