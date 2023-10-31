import time
import math

def my_prime(numb):
    prime_lst=list()
    prime_lst.append(2)
    cnt=1
    inner=1
    ii=3
    while ii<numb:                  #all primes under numb
        check=True
        for jj in prime_lst:
            if ii%jj!=0:
                continue
            else:
                check=False
                break
        if check:
            prime_lst.append(ii)
            inner+=1
        ii+=2

    #print(cnt,prime)
        cnt+=1
    print('count: ',cnt,'inner: ',inner)
    return prime_lst

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
    print('count: ',cnt,'inner: ',inner)
    return prime

numb=int(input('Enter number:'))
#t0=time.time()
#prime1=[my_prime(numb)
#t1=time.time()
#print("MY PRIME\n",len(prime1),' time:',t1-t0)

#t2=time.time()
prime2=sieve_prime(numb)
#t3=time.time()
#print("SIEVE PRIME\n",len(prime2),' time:',t3-t2)
print(prime2,prime2)
