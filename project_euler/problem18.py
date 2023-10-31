handle=open('problem18.txt')
total_list=[]
for line in handle:
    line=line.split()
    total_list.append(line)

print(total_list)

ii=len(total_list)
ii-=2

while ii>=0:
    jj=0
    while jj<=ii:
        total_list[ii][jj]=max(int(total_list[ii][jj])+int(total_list[ii+1][jj]),int(total_list[ii][jj])+int(total_list[ii+1][jj+1]))
        jj+=1
    ii-=1
print(total_list)
asd=input()
