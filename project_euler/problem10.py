import math
numb=30
prime_lst=list()
prime=list()
sum=0
for n in range(2,numb+1):
    prime_lst.append(n)
cnt=1
inner=1
ii=0
length=len(prime_lst)
rng=int(math.sqrt(numb))
while ii<=rng:
    curr=prime_lst[ii]
    if curr==0:
        ii+=1
        continue
    for jj in range(2,int(numb/curr)+1):
        if (ii+2)*jj-1>length:
            break
        prime_lst[(ii+2)*jj-2]=0
        inner+=1
    print(prime_lst)
    ii+=1
    cnt+=1
for num in prime_lst:
    if num==0:
        continue
    sum+=num
print('count: ',sum,'inner: ',inner)
