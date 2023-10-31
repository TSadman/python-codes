lst_coll=list()
collated=list()
maximum=0
png=24
for ii in range(png):
    lst_coll.append(ii+1)
    collated.append(0)
for jj in range(png):
    cnt=1
    if lst_coll[jj]==0:
        continue
    num=jj+1

    while True:
        if num==1:
            break
        if num%2==0:
            num/=2
            cnt+=1
        else:
            num=3*num+1
            cnt+=1
        if num<png and lst_coll[int(num-1)]!=0:
            lst_coll[int(num-1)]=0

    if cnt>maximum:
        maximum=cnt
        output=jj+1
    print(jj,maximum,output,lst_coll[jj-5:jj+5])
print(maximum,output)
