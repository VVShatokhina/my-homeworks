import re
import os

lst = os.listdir('texts')
arr = []
unique = []
for f in lst:
        if re.search(r'[0-9]+',f):
            arr.append(f)

for papka in arr:
        if papka not in unique:
            unique.append(papka)
            
print(len(arr))
