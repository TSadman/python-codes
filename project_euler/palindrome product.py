def chk_factor(num):
    start_num=100
    strt=start_num
    end_num=999
    
    # check for 2
    if num%2==0:
        key=1
    else:
        key=2
        start_num+=1
    
    while True:
        if start_num>end_num:
            break
        modulus=num%start_num
        division=num/start_num
        start_num=start_num+key
        if division<strt or division>end_num:
            continue
        if modulus==0:
            
            return True
    
    return False

def chk_nxt_pal(num):
    chk_num=num-1
    while True:
        str_num=str(chk_num)
        if str_num==str_num[::-1]:
            return chk_num
        chk_num-=1
    
end=100**2
start=999**2
curr_num=start
ii=1
while True:
    pal_num=chk_nxt_pal(curr_num)
    curr_num=pal_num
    if curr_num<end:
        break
    check_fact=chk_factor(curr_num)
    if check_fact:
        output=pal_num
        break
    print(ii)
    ii+=1
print(output)