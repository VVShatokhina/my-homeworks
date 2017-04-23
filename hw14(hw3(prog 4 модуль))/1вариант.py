import os

count = 0
for root, dirs, files in os.walk('.', topdown=False):
    for g in dirs:
        count +=1
print('максимальная глубина папки:', count)
