import random

def create_dictionary():
    f = open('p.txt', 'r', encoding = 'UTF-8')
    a = ()
    b = []
    for line in f:
        line = line.strip('\ufeff\n')
        a = tuple(line.split(';'))
        b.append(a)
    d = dict(b)
    f.close()
    return d

def one_turn(d, hint, n_attempts):
    first_guess = input('Угадайте слово:\n' + hint + '\n')
    if first_guess == d[hint]:
        what_next = input('Правильно!\nСыграть еще - введите что-либо\nЗакончить - нажмите enter')
    else:
        while n_attempts != 0:
            guess = input('Попробуйте еще раз.\nПопыток осталось: ' + str(n_attempts) + '\n(Сдаться - нажмите enter):\n')  
            if guess == d[hint]:
                what_next = input('Правильно!\Сыграть еще - введите что-либо\nЗакончить - нажмите entern'+'\n***\n')
                break
            elif guess == '':
                n_attempts = 0
            else:
                n_attempts -= 1
    if n_attempts == 0:
        what_next = input('Вы проиграли. Это было слово \'' + d[hint] +'\'\nСыграть еще - введите что-либо\nЗакончить - нажмите enter\n***\n')
    return what_next

def the_game():
    print('Игра "Слова"')
    while True:
        d = create_dictionary()
        hint = random.choice(list(d.keys()))
        n_attempts = len(d[hint]) - 1
        what_next = one_turn(d, hint, n_attempts)
        if what_next == '':
            print('До свидания.') 
            break
def main():
    the_game()

if __name__ == '__main__':
    main()
