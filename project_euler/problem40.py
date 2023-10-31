position=[1,10,100,1000,10000,100000,1000000]

ii=1
total=''

while ii<=10**(len(str(max(position)-1))):
    total=total+str(ii)
    ii=ii+1

for num in position:
    print(total[num-1])