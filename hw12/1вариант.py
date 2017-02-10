import re

def reads_file():
    f = open('komar.txt', 'r', encoding = 'UTF-8')
    text = f.read()
    f.close()
    return text

def new_file(result):
    f = open('slon.txt', 'w', encoding = 'UTF-8')
    f.write(result)
    f.close()
    
def change(text):
    text1 = re.sub('комар((а(м(и)?|х)?|ы|о(в|м)|е|у)|( |\.|,|\)|:|;|\?|!|\n|\t\|»|-))', r'слон\1', text)
    text2 = re.sub('Комар((а(м(и)?|х)?|ы|о(в|м)|е|у)|( |\.|,|\)|:|;|\?|!|\n|\t\|»|-))', r'Слон\1', text1)
    return text2

def main():
    new_file(change(reads_file()))

if __name__ == '__main__':
    main()
