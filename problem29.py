lst=list()
low_lim=2
up_lim=100
for a in range(low_lim,up_lim+1):
    for b in range(low_lim,up_lim+1):
        num=a**b
        #print(num)
        if num in lst:
            continue
        lst.append(num)
lst=sorted(lst)
print(len(lst))
