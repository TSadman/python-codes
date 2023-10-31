import time
import math

t0=time.time()
total_fact=list()
ori_num=600851475143
num=ori_num
max_fact=1
#max_ori_num=int(ori_num**0.8)+1
print(ori_num)

if num%2==0:                            #check if 2 is a factor
    total_fact.append(2)
    num=num/2
    max_fact=2                          #max_fact is used to determine the maximum divisible prime

while True:                             #itirates number untill its no longer divisible by 2
    if num%2!=0:
        break
    num=num/2

test_num=3
test_inner=False

while True:                                             #3 theke start kore 3,5,7.... ebe check kore. 1st e check kore number divisible kina, divisible hole main num ke devide kore dey, pore check kore prime kina, prime hole rakhe, naile chere dey
    #print(total_fact,test_num,num)
    if chk_num:
        test_num_logic=True
        if test_num>=num:                                    #step-4: check if the loop should be stopped
            test_inner=True
            test_num=num

        if test_inner:
            if test_num==1: break                                         #if the final number arrives, checks if its prime and breaks
            if ori_num%test_num==0:
                total_fact.append(test_num)
            print(total_fact,num)
            break

        if num%test_num==0:                             #step-1: checks if number is divisible
            num=num/test_num
            while num%test_num==0:
                num=num/test_num
        else:
            test_num+=2
            continue

        for ii in total_fact:               #step-2: checks if the current number is prime(the idea is that previous prime gular respect e divisible kina)
            if test_num%ii==0:
                test_num_logic=False
                break

        if test_num_logic:                  #step-3: if step-2 finds number is prime, it adds here
            total_fact.append(test_num)
            max_fact=test_num
        test_num+=2

t1=time.time()
print(total_fact,t1-t0)
print(max_fact)
