word=input('Введите слово: ')
words=[]
while word !='':
    for i in word:
        i=word[::-1]
        for n in i:
             n=i[:-3]+i[-2]+i[-1]
    words.append(n)
    word=input('Введите слово: ')
for m in words:
    print(m)
   
