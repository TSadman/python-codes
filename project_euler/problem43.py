from itertools import permutations

perm= permutations([0,1,2,3,4,5,6,7,8,9])

all_num=list()

'''for ii in perm:
    num=''
    for jj in ii:
        num=num+str(jj)
    all_num.append(num)
    '''
total=0

for ii in perm:
    if ii[0]==0: continue
    if ii[3]%2!=0: continue
    if (ii[2]+ii[3]+ii[4])%3 != 0: continue
    if ii[5]%5 != 0: continue
    if (ii[6]+10*ii[5]+100*ii[4])%7 != 0: continue
    if (ii[7]+10*ii[6]+100*ii[5])%11 != 0: continue
    if (ii[8]+10*ii[7]+100*ii[6])%13 != 0: continue
    if (ii[9]+10*ii[8]+100*ii[7])%17 != 0: continue
    num=0
    for x in range(10): num=num+10**(x)*ii[9-x]
    print(num)
    total=total+num

print(total)    