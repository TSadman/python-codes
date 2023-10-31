#first check all primes under the limit
#make dict() of all primes and count max
#calculate maximum count of these primes in every number leading upto limit
#factorize the numbers

#funcions needed: factorize(num), check prime(limit), use dict() in main loop

import math
import time
def sieve_prime(numb):
    prime_lst=list()
    prime=list()
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
            #print(prime_lst)
            inner+=1
        ii+=1
        cnt+=1
    for num in prime_lst:
        if num==0:
            continue
        prime.append(num)
    return prime

def get_factors(num,prime):
    factor=list()
    number=num
    temp_prime=prime[:]
    #print(prime,temp_prime)

    while True:
        if temp_prime==[]:
            break
        ii=temp_prime[0]
        #print(ii,temp_prime)
        if number%ii==0:
            factor.append(ii)
            number=number/ii
            continue
        else:
            temp_prime.pop(0)
        if len(temp_prime)==0:
            break
    return factor

num=int(input('Enter range:'))
t0=time.time()
total=1
hist_prime=dict()
final_hist=dict()
t2=time.time()
prime=sieve_prime(num)
t3=time.time()
curr_list=list()
for ii in prime:
    final_hist[ii]=0
"""
for ii in range(2,num+1):
    #print(prime)
    curr_list=get_factors(ii,prime)
    #print(ii,curr_list)
    hist_prime={}
    for jj in curr_list:
        if jj in hist_prime:
            x=hist_prime[jj]
        else:
            x=0
        hist_prime[jj]=x+1

    #print(hist_prime)
    for key,value in hist_prime.items():
        if final_hist[key]<value:
            final_hist[key]=value
    #print(final_hist)

for key,value in final_hist.items():
    #print(key,'**',value,':',total)
    total=total*key**value
"""
t1=time.time()
print(t1-t0,t3-t2)
#print('total:',total,'time:',t1-t0,'prime:',final_hist)
