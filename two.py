b='1101'
i=0
num=0
while b!='':
    i=i*2+(ord(b[0])-ord('0'))
    b=b[1:]
    #num+=1
    b=b[1:]
    #print(num,':','i:',i,'b:',b)
print(i)
