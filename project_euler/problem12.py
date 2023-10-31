import math

def next_tri(n):
    num=(-1+math.sqrt(1+8*n))/(2)
    while num!=int(num):
        #print(n,num)
        n+=1
        num=(-1+math.sqrt(1+8*n))/(2)
    #print(n,num)
    return n

def factors(n):
    num=0
    root=math.sqrt(n)
    for ii in range(1,int(root)):
        if n%ii==0:
            num+=1
    num*=2
    if n%int(root)==0:
        num+=1
    return num

minimum=7*11*2**4*3**4*5**4
init_tri=next_tri(minimum)
num=int((-1+math.sqrt(1+8*init_tri))/(2))

while True:
    num+=1
    init_tri+=num
    factor=factors(init_tri)
    if factor>500:
        break
print(init_tri)
