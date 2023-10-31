import math
lst=list()
lst_temp=list()
word=None
#while word!='done':
#    word=input('Enter num:')
#    lst.append(word)
lst=['0','1','2','3','4','5','6','7','8','9']
length=len(lst)-1
kk=length
temp=0
mm=0
for ii in range(length+1):
    #print('beginning',lst,kk,temp)
    aa=0
    for jj in range(kk+1):
        aa=aa+math.factorial(kk)
        if (temp+aa)>=1000000:
            jj=jj+ii
            aa=aa-math.factorial(kk)
            #print('*',jj,aa)
            break
        #print('***',jj,aa)
    kk-=1
    mm+=1
    #print('middle',lst,jj,ii,aa,kk)
    t=lst.pop(jj)
    lst.insert(ii,t)
    temp+=aa
    #print('end',lst,temp)
print(lst)
