def check_prime(num):
    limit=int(num**0.5)
    if num%2==0: return True
    for ii in range(3,limit+1,2):
        if num%ii==0:
            return True
    return False

def list2num(lst):
    max_num=0
    for n in range(len(lst)):
        max_num=max_num+(10**n)*lst[n]
    return(max_num)

pan_list=list()
sum=0
for ii in range(1,10):
    sum=sum+ii
    if sum%3==0:
        continue
    lst=list()
    for jj in range(1,ii+1):
        lst.append(jj)
    pan_list.append(lst)

largest=pan_list[-1]

length=len(largest)

prime_list=list()

check=True
number=list2num(largest)+2
n=set(largest)

while check:
    number=number-2
    asd=str(number)
    nd=[]
    for kk in asd:
        nd.append(int(kk))
    nd=set(nd)
    if nd!=n: continue
    check=check_prime(number)
    