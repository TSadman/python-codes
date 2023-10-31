def finding_b(p,a):
    b=(p**2-2*a*p)/(2*p-2*a)
    return b

p=2
intrt=list()

while p<=1000:
    a=1
    listlen=list()
    maximum=int(p/2)
    while a<maximum:
        b=finding_b(p,a)
        if b==0 or b-int(b) != 0:
            a=a+1
            continue
        b=int(b)
        if b<maximum:
            maximum=b
        c=(a**2+b**2)**0.5
        temp=[a,b,int(c)]
        listlen.append(temp)
        a=a+1
    if len(listlen)!=0:
        count=[p, len(listlen)]
        intrt.append(count)
    p=p+1

lst=list()

for ii in intrt:
    lst.append(ii[1])

print(max(lst))

for ii in intrt:
    if ii[1]==max(lst):
        print(ii[0])
