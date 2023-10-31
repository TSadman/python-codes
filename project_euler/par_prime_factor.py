from multiprocessing import Pool

prime=list()
prime.append(2)
prime.append(3)

def chk_prime(num):
    check=True
    for ii in prime:
        if num % ii != 0:
            continue
        else:
            check=False
            break
    if check:
        return num
    else:
        return
limit=10000
number=3

tmp_lst=list()

while number<limit:
    if __name__=='__main__':
        with Pool(5) as p:
            tmp_lst=p.map(chk_prime, [number,number+2,number+4,number+6,number+8,number+10])
            prime=prime+tmp_lst
            print(tmp_lst)
    number=number+12
#number=chk_prime(prime,5)
#prime=prime+number
