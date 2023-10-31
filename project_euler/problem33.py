import math

num=1
den=1

for ii in range(10,100):
    for jj in range(10,100):
        if ii>=jj: continue
        a=set(str(ii))
        b=set(str(jj))
        z=a.intersection(b)
        if len(a)!=2 or len(b)!=2 or len(z)!=1 or '0' in z:
            continue
        a=int(list(a-z)[0])
        b=int(list(b-z)[0])
        if b==0: continue
        if a/b==ii/jj:
            print(ii,'/',jj)
            num=num*a
            den=den*b

print(num,den)

print(den/math.gcd(num,den))