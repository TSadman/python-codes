cycle_count=dict()

for  d in range(1,1001):
    number=list()
    number2=list()
    num=1
    while True:
        temp=int(num/d)
        num=(num%d)*10
        if (num/10 in number2) or num==0:
            number.append(temp)
            break
        number.append(temp)
        number2.append(num/10)
    if num==0:
        continue
    rec_start=number2.index(num/10)+1
    cycle_count[d]=len(number)-rec_start
    
key=list(cycle_count.keys())

val=list(cycle_count.values())

print(key[val.index(max(val))])