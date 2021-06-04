import os
from random import choice

fileName = 'units.txt'

if not os.path.exists(fileName) :
    file = open(fileName, 'x')
    file.close()

def writer(words):
    file.write(words)

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print('1.Add words\n2.Learn by heart')

if input('>> Enter the command: ') == '1':
    print("Enter the words in the 'En-Uz' view:\n(enter 'done' to finish)")
    while 1:
        file = open(fileName, 'a')
        word = input('>>> ')
        if word == 'done' :
            file.close(); break
        writer(word + '\n')

else:
    words = []
    file = open(fileName)
    for i in file:
        words.append(i)
    file.close()

    while 1:
        if len(words) == 0 : break

        line = choice(words)
        words.remove(line)
        clearConsole()
        print(line.split('-')[1].strip(), end='')
        if input() == "" :
            print(line.split('-')[0])
        if input() == "" :
            clearConsole()
            continue
        if input() == "end" : break
