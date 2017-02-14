import re 

open('isl.txt', 'r', encoding = 'UTF-8') 
lines = 0
for line in open('isl.txt'):
        lines += 1
result = str(lines)
open('out.txt', 'w').write(result)
print("#1 Результат записан")

d = {}
reg = '.*lemma=/"[a-z]'
r = re.search(reg, 'isl.txt')
d.keys(r)

reg2 = '.*type="[a-z]'
r2 = re.search(reg2, 'isl.txt')
d.value(r2)

for key, value in d.items():
    print(key,value)





