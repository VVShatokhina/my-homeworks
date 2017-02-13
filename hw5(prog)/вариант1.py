f = open('дз.txt')
for i in f:
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
 
    print(i, word,'сл.')
f.close()
