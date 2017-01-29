import re

with open('tom.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().replace('\n', '').lower()
    words = text.split()
    arr = []
    unique = []
    for word in words:
            word = word.strip('.,!?^$@#:;_- []()\|/\n\ufeff')
            check = re.search('откр(ыва|ы(я.*|ю.*|е.*|й.*|ю.*|ем.*|ешь.*|ете.*|ет.*|ют.*|та.*|т.*|то.*|ты.*|л.*|ли.*|лся.*|лась.*|лася.*|лись.*|ть.*|ться.*|я.*|ющим.*|ющими.*|ющего.*|ющей.*|ющих.*|ющие.*|вши.*|того.*|тую.*|тых.*|тым.*))', word)
            if check != None:
                arr.append(word)
            else:
                continue
    for word in arr:
        if word not in unique:
            unique.append(word)
            
    print('\n'.join(unique))
            
