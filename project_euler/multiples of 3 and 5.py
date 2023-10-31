rng=1000
summation=0
num=1
ii=1
a=1
while True:
    mul_3=3*ii
    if mul_3>=rng:
        break
    summation=summation+mul_3
    ii+=1
    #print(mul_3)
num=1
ii=1
while True:
    mul_5=5*ii
    if mul_5>=rng:
        break
    ii+=1
    if mul_5%3==0:
        continue
    #print(mul_5)
    summation=summation+mul_5
print(summation)