list_cub = []
for i in range(1, 1001, 2):
    list_cub.append(i ** 3)
print('список кубов: ', list_cub)

sum = 0
for idx in list_cub:
    result = 0
    count = idx
    while idx > 0:
        result += idx % 10
        idx = idx // 10
    if result % 7 == 0:
        sum += count
print('Сумма цифр с делением нацело на 7: ', sum)

sum_2 = 0
for idx in list_cub:
    seventeen = 17
    idx_sev = seventeen + idx
    result = 0
    count = idx_sev
    while idx_sev > 0:
        result += idx_sev % 10
        idx_sev = idx_sev // 10
    if result % 7 == 0:
        sum_2 += count
print('Сумма цифр на c прибовлением 17: ', sum_2)