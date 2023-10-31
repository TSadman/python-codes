import urllib.request
import xml.etree.ElementTree as ET

xml_file=open('xml_file.xml','w')
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.xml')
for line in fhand:
    ln=line.decode().strip()
    ln+='\n'
    xml_file.write(ln)
    #print(ln)
xml_file.close()

mytree=ET.parse('xml_file.xml')
myroot=mytree.getroot()
sum=0
for x in myroot.findall('comments/comment'):
    item=x.find('count').text
    sum+=int(item)
    print(item)
print(sum)
