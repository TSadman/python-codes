import math

maximum=int(input('Enter maximum number: '))

def div_tot(n):
    sum=0
    lim=math.ceil(math.sqrt(n))
    for ii in range(1,lim):
        if n%ii==0:
            #print('*****',ii)
            sum+=ii
            if ii==1: continue
            sum+=(n/ii)
        #print(sum,ii)
    if math.sqrt(n)==lim:
        sum+=(lim)
    return int(sum)
'''
ami_sum=list()
sum=0
for ii in range(1,maximum+1):
    temp=div_tot(ii)
    ami_sum.append(temp)
print(len(ami_sum))

for jj in range(maximum):
    #print(jj)
    num=ami_sum[jj]
    #print(num)
    if num>maximum: continue
    if ami_sum[num-1]==num:
        sum+=(jj+1)
    print(jj+1,ami_sum[num-1],num,sum)
print(sum)
'''

sum=0
for ii in range(1,maximum+1):
    temp=div_tot(ii)
    if temp==1 or temp==ii: continue
    temp2=div_tot(temp)
    if temp2==ii:
        sum+=ii
    #print(ii,temp,temp2,sum)
print(sum)

print(div_tot(12))
