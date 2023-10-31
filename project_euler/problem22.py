name=list()
handle=open('problem22.txt')
for line in handle:
    line=line.split(',')
    for ii in line:
        name.append(ii[1:-1])

length=len(name)

for ii in range(length-1):
    for jj in range(length-1):
        if name[jj]>name[jj+1]:
            temp=name[jj]
            name[jj]=name[jj+1]
            name[jj+1]=temp


#name=['COLIN']
num=1
sum=0
for word in name:
    temp_sum=0
    for ii in word:
        temp_sum+=(ord(ii)-64)
        #print(ord(ii)-64)
    #print(temp_sum)
    sum+=num*temp_sum
    num+=1

print(sum)
