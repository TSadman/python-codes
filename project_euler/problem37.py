import time
t0=time.time()
prime={2,3,5,7}

def if_prime(num):
    for ii in prime:
        if num%ii==0:
            return False
    prime.add(num)
    return True


def trun_prime(num):
    string=str(num)
    length=len(string)
    ii=0
    while ii<length:
        temp_str_l2r=string[ii:]
        temp_str_r2l=string[:length-ii]
        if int(temp_str_l2r) not in prime or int(temp_str_r2l) not in prime:
            return False
        ii=ii+1
    return True
    
start_num=11

count=0
trun_num=list()

x=trun_prime(3797)

while count<11:
    check=if_prime(start_num)
    if check:
        trun_check=trun_prime(start_num)
        if trun_check:
            trun_num.append(start_num)
            count=count+1
    start_num=start_num+2
t1=time.time()
       
print(trun_num,'sum:',sum(trun_num),'time:',t1-t0)