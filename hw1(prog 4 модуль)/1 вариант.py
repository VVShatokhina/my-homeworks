import re

with open('great.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().replace('\n', '').lower()
    words = text.split()
    arr = []
    for word in words:
            word = word.strip('.,!?^$@#:;_- []()\|/\n\ufeff')
            arr.append(word)
other_words = [w.lower() for w in arr if len(w) >= 7]
other_words
d = {wo : len(wo) for wo in other_words}
for i in d.items():
    print('{} ---- {}'.format(i[0], i[1]))

