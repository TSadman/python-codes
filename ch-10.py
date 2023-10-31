handle=open('one.txt')
hour=list()
dic_time=dict()
final=dict()
dct=dict()
val=list()
for line in handle:
    line=line.split()
    if len(line)<1: continue
    if line[0]=='From':
        time=line[5]
        hour.append(time[:2])
for ii in hour:
    if ii in dic_time:
        dic_time[ii]+=1
    else:
        dic_time[ii]=1
