total_currency=[0,1,2,3,4,5,6,7,8,9]

def permutation(lst):

    if len(lst)==0:
        return []

    if len(lst)==1:
        return [lst]

    temp_list=list()

    for ii in range(len(lst)):
        m=lst[ii]
        rem_list=lst[:ii]+lst[ii+1:]

        for p in permutation(rem_list):
            temp_list.append([m]+p)

    return temp_list

handle=open('permutation.txt','w')
cnt=0
handle.write(str(permutation(total_currency)))
#for jj in permutation(total_currency):

#    handle.write(str(jj))

#    cnt+=1
#    if cnt==1000000:
#        break
#        print(jj)
#        cnt=0
#    handle.write('\n')

handle.close()
