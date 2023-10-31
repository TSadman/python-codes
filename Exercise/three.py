stuff=list()
another=list()
while True:
    word=input('Enter number: ')
    if word=='out':
        break
    word=int(word)
    stuff.append(word)
print(stuff)
num=int(input('Enter max num: '))
for i in stuff:
    if i<num:
        another.append(i)
print(another)
