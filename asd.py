import re
fhand=open('regex_sum_735403.txt','r')
t=''
for line in fhand:
    t+=line

h=list()
print(t,'*************')
h= re.findall('[0-9]+',t)
print(h)
w=list()
for a in h:
	w.append(int(a))
print(w)

z=0
for b in w:
	z=z+b
print("SUM:",z)
