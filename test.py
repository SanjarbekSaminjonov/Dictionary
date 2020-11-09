import os

if not os.path.exists('test.txt') :
    file = open('test.txt', 'x')
    file.close()

def writer(word):
    file.write(word)

print('1.Add words\n2.Learn by heart')

if input('>> Enter the command: ') == '1':
    print("Enter the words in the 'En-Uz' view:\n(enter 'done' to finish)")
    while 1:
        file = open('test.txt', 'a')
        word = input('>>> ')
        if word == 'done' : file.close(); break
        writer(word + '\n')


else:
    print('We are beginning...\nPress enter___')
    file = open('test.txt')

    for line in file:
        print(line.split('-')[0])
        if input() == "" :
            print(line.split('-')[1])
        if input() == "" : continue
