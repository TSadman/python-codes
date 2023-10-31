
import time
from itertools import permutations

def circular_prime_check(num): 
    num=str(num)
    temp=num+num
    perms=list()
    aa=len(num)
    if aa==1:
        return True
    for ii in range(len(num)):
        jj=int(temp[ii:ii+aa])
        if jj in all_primes_set:
            continue
        else:
            return False
    return True
    
def primes_under(num):
    all_num=list()
    prime_num=list()
    for ii in range(2,num+1):
        all_num.append(ii)
    for ii in range(num-1):
        aa=all_num[ii]
        if aa==0:
            continue
        mul=2
        while mul*aa<=num:
            all_num[mul*aa-2]=0
            mul=mul+1
    for ii in all_num:
        if ii!=0:
            prime_num.append(ii)
    return prime_num

t0=time.time()
all_primes=primes_under(1000000)
all_primes_set=set(all_primes)
print(len(all_primes))
circular_prime=list()
t2=time.time()

for number in all_primes:
    if circular_prime_check(number):
        circular_prime.append(number)

t1=time.time()

print(len(circular_prime),'\t time taken: ',t1-t0,t2-t0)
'''
#from Euler import prime_sieve
L, s = 1000, set('024568')

def prime_sieve(n):
	sieve = [True] * (n//2)
	for i in range(3,int(n**0.5)+1,2):
		if sieve[i//2]:
			sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
	return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def rotate(s):
    return [s[n:] + s[:n] for n in range(1, len(s))]

primes = set(['2','5']+[str(p) for p in prime_sieve(L) if not set(str(p)).intersection(s)])

n_circular_primes = sum(all(pr in primes for pr in rotate(p)) for p in primes)
print("Project Euler 35 Solution =", n_circular_primes)
'''