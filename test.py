alp='abcdefghijklmnopqrstuvwxyz'

pp=list()

for ii in alp:
    pp.append(ii)
#print(pp)

lst=list()

for ii in range(26):
    tempList=list()
    for jj in range(len(pp)):
        zz=ii+jj+1
        if zz>25:
            zz=zz-26
        temp=pp[zz]
        tempList.append(temp)
    #print(tempList)
    lst.append(tempList)
#print(lst)

given='vagreaangvbany uvtu grpuabybtl fheirl---------vaqvtb, uraan, gnatrevar naq fhasybjre------------vagrearg uvfgbel, grpuabybtl, naq frphevgl---------vagreany uvtu grpuabybtl fbyhgvba'

decryptList=list()

def indexCount(lst,data):
    ii=0
    for jj in lst:
        if jj==data:
            return ii
            break
        ii=ii+1

def addtwo(num):
    return num+2

count=1

for ii in lst:
    index=list()
    for jj in given:
        temp=indexCount(ii,jj)
        index.append(temp)
    #print(index)
    if count!=13:
        count+=1
        continue
    print(count,'.\t',end='')
    for kk in index:
        if kk is None:
            print(' ',end='')
            continue
        print(pp[kk],end='')
    count+=1
    print('')
