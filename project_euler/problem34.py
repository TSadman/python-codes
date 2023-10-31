import math

def digit_factor_sum(num):
    total=0
    num_str=str(num)
    for digit in num_str:
        total=total+math.factorial(int(digit))
    if total==num and len(num_str)>1:
        return True
    else:
        return False

max_limit=math.factorial(9)


total=0    
for num in range(1,max_limit):
    check=digit_factor_sum(num)
    if check:
        total=total+num
        
print(total)