import numpy

def func_prime(numb):
    ii=3
    #cnt=1
    prime=list()
    while ii<numb:                  #all primes under numb
        check=True
        for jj in prime:
            if ii%jj!=0:
                continue
            else:
                check=False
                break
        if check:
            prime.append(ii)
        ii+=2
        print(ii)
    #print(cnt,prime)
    #cnt+=1
    return prime

def rwh_primes(n):
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * np.unit32(n/3)
    sieve[0] = False
    for i in range(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n/3-correction) if sieve[i]]


import math
import time

numb=600851475143
lar=list()

t0=time.time()

numb=numb
prime=rwh_primes(numb)
print(len(prime), prime)

t1=time.time()
for number in prime:                #check if factor
    if numb%number==0:
        lar.append(number)
    #print(lar)

t2=time.time()
print(max(lar),len(prime))
print(t2-t1,t1-t0)
