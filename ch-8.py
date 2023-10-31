handle=open('one.txt')
lst=list()
count=0
for line  in handle:
    line=line.rstrip()
    line=line.split()
    if len(line)<=0:
        continue
    if line[0] == 'From':
        lst.append(line[1])
        count=count+1
        print(line[1])
print(count)
