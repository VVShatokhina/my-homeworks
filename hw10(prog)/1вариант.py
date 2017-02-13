import re

def read():
    f = open('c.html', 'r', encoding = 'UTF-8')
    text = f.read()
    f.close()
    return text

def find(text):
    s = re.search('\<td[^а-яА-Я].*\>Столица\<[^а-яА-Я]*([а-яА-Я].*\>+)', text)
    result = ''
    if s:
        result = s.group(1)
    return result

def add(result):
    f = open('capital.txt', 'a')
    f.write(result)
    f.close()

def main():
    text = read()
    result = find(text)
    add(result)

if __name__ == '__main__':
    main()
