import re
handle=open('regex_sum_406245.txt')
sum=0
for line in handle:
    words=re.findall('[0-9]+',line)
    for number in words:
        sum=sum+int(number)
print(sum)
