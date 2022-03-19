for i in range(1, 101):
    count = i % 10
    if count == 1:
        print(i, 'процент')
    elif i > 10 and i < 15:
        print(i, 'процентов')
    elif count > 1 and count < 5:
        i = i > 10 and i < 15
        continue
        print(i, 'процента')
    else:
        print(i, 'процентов')
