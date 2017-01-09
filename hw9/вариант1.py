import random 

def file_op(name):
    f = open(name,'r')
    ar = f.read().split(' ')
    f.close()
    return(ar)

def noun():
    ar = file_op("noun.txt")
    return random.choice(ar) + ' '

def verb():
    ar = file_op("verb.txt")
    return random.choice(ar) + ' '

def adj():
    ar = file_op("adj.txt")
    return random.choice(ar) 

def obj():
    ar = file_op("obj.txt")
    return random.choice(ar)  

def punct():
    ar = file_op("punct.txt")
    return random.choice(ar) + ' '


def verse1():
    return noun() + verb() + adj() + punct()

def verse2():
    return noun() + verb() + adj() + ' ' + obj() + punct()

def verse3():
    return noun() + verb() + adj() + punct()

def main():
    print("***")
    print(verse1().capitalize() + "\n" + verse2().capitalize() + "\n" + verse3().capitalize())

main()
