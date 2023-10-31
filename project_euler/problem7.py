import math

numb=int(input('NUMB:'))
prime_lst=list()
prime_lst.append(2)
cnt=1
inner=1
ii=3
while cnt<numb:                  #all primes under numb
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
        cnt+=1
    ii+=2

#print(cnt,prime)
print('count: ',cnt,'inner: ',inner)
print(prime_lst)
