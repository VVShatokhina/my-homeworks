f = open('text.txt', encoding='utf-8')
for line in f:
    len(line.split(' '))
    max_len = max(len(words) for words in line.split())
    if max_len < 10:
        print(line)
