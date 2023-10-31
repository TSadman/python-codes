import urllib.request
import json

json_file=open('json_file.txt','w')
#json_file.write("'''")
url=input('Enter url:')
fhand = urllib.request.urlopen(url)
for line in fhand:
    ln=line.decode().strip()
    ln+='\n'
    json_file.write(ln)
    #print(ln)
#json_file.write("'''")
json_file.close()

with open('json_file.txt') as json_file:
    data=json.load(json_file)
sum=0
for ii in range(len(data['comments'])):
    sum+=data['comments'][ii]['count']
print(sum)
