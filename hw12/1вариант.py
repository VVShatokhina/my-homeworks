import re

with open('Украина — Википедия.html', 'r', encoding = 'utf-8') as f:
    text = f.read()
    for word in text:
        r = re.search('\<td[^а-яА-Я]*Столица.*[^а-яА-Я]*([а-яА-Я]+)', word)
        group = ''
        if r:
            group = r.group(1)

def add_to_file(group):
    f = open('capital.txt', 'a')
    f.write(group)
    f.close()

def main():
    add_to_file(group)
    
if __name__ == '__main__':
    main()
