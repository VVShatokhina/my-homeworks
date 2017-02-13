s = input('Введите слово: ')
for i in s[1:100:2]:
    if i == 'а':
        continue
    elif i == 'к':
        continue
    print(i)
