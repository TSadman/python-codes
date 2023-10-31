def letter2num(letter):
    lst="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return lst.index(letter)+1

handle=open('problem42.txt')

for document in handle:
    words=document.split(',')

word=list()

for ii in words:
    ii=ii[1:-1]
    word.append(ii)

count=0

for ii in word:
    num=0
    for jj in ii:
        temp=letter2num(jj)
        num=num+temp
    n=(-1+(1+8*num)**0.5)/2
    if n==int(n):
        count=count+1
    
print(count)