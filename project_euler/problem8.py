handle=open('problem8.txt')
data=''
for line in  handle:
    data+=line[:-1]
length=len(data)

ii=0
num=int(input('Enter adjacent  numbers:'))
max=0
max_lst=list()

while ii<=(length-num):
    lst=[]
    temp=1
    for cnt in range(0,num):
        temp*=int(data[ii+cnt])
        lst.append(data[ii+cnt])
    if temp>max:
        max=temp
        max_lst=lst
    print(max,max_lst)
    ii+=1
print(max,max_lst)
