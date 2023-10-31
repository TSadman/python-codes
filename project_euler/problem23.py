import math
def abundant_chk(n):
    #print('*******',n)
    if n==1: return False
    sum=1
    maximum=math.ceil(math.sqrt(n))
    for ii in range(2,maximum):
        if n%ii==0:
            sum+=(ii+n/ii)
        #print(ii,sum,n/ii)
    if math.sqrt(n)==maximum:
        sum+=maximum
        #print(sum,maximum)
    if sum>n:
        return True
    else:
        return False

abundant=list()

for ii in range(2,28124):
    if abundant_chk(ii):
        abundant.append(ii)

#print(abundant)
sum=0
for ii in range(1,28124):
    total=0
    for jj in abundant:
        temp=ii-jj
        if temp<1:
            sum+=ii
            break
        if abundant_chk(temp):
            print(ii,temp)
            break
print(sum)
