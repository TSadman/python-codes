fibb_num=1
sum_fib=0
fibb_add=0
rng=4000000
while True:
    temp=fibb_num
    fibb_num=fibb_num+fibb_add
    fibb_add=temp
    if fibb_num>rng:
        break
    if fibb_num%2==0:
        sum_fib=sum_fib+fibb_num
    #print(fibb_num,sum_fib)
print(sum_fib)