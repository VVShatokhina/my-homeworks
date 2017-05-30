import re

with open('zamok.txt', 'r', encoding = 'UTF-8') as f:
    text = f.read()
    words = text.split()
for word in words:
    s1 = re.search('^[А-Я]\.\s^[А-Я][^\s\d]+', word)
for wordd in words:
    s2 = re.search('^[А-Я]\.\s^[А-Я]\.\s[А-Я][^\s\d]', word)
for worddd in words:
    s3 = re.search('^[А-Я]\s^[А-Я][^\s\d]', word)
print('инициал + фамилия:', word)
print('инициалы + фамилия:', wordd)
print('имя + фамилия:', worddd)
