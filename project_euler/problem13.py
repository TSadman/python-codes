handle=open('problem13.txt')
sum=''
lst=list()
cnt=1
rem=0
for line in handle:
    for ii in range(50):
        if cnt==1:
            lst.append(int(line[ii]))
            continue
        lst[ii]=lst[ii]+int(line[ii])
    cnt+=1
print(cnt,lst)

for jj in range(50):
    num=rem+lst[49-jj]
    digit=int(num%10)
    if jj==49:
        sum+=str(num)[::-1]
        print(jj,rem,num)
        break
    print(jj,rem,digit,lst[49-jj])
    rem=int((num-digit)/10)
    sum+=str(digit)
print(sum[-1:-11:-1])
