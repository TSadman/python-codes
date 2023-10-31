b=0
c=0
a=1
triplet=list()
max=12
while a<max/3:

    b=a+1
    c=max-a-b
    while b<c:
        #print(a,b,c)
        c=max-a-b
        if a**2+b**2==c**2:
            print(a*(b*c))
            b+=1
            continue
        b+=1
    a+=1
