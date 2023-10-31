import xml.etree.ElementTree as ET
import xlwt
from xlwt import Workbook

wb=Workbook()
s1=wb.add_sheet('Send money')
s2=wb.add_sheet('Cash in')

data=ET.parse('sms.xml')
tree=data.getroot()

alldata=tree.findall('sms')
length= len(alldata)
print(length)

messages=[]
num1=0
num2=0
column1=0
column2=0

for ii in range(0,length):
    message=alldata[ii].get('body')
    message=message.split()

    if message[0]=='You' and message[1]=='have':
        message[4]=message[4].replace(',','')
        try:
            taka=float(message[4])
        except:
            continue
        if taka>1000 or taka<300:
            continue
        s1.write(num1,column1+0,message[6])
        s1.write(num1,column1+1,message[-4])
        s1.write(num1,column1+2,taka)
        s1.write(num1,column1+3,message[-2]+'  '+message[-1])
        num1=num1+1
        if num1==250:
            num1=0
            column1=column1+6

    elif message[0]=='Cash' and message[1]=='In':
        message[3]=message[3].replace(',','')
        try:
            float(message[3])
        except:
            continue
        s2.write(num2,column2+0,message[5])
        s2.write(num2,column2+1,message[-7])
        s2.write(num2,column2+2,float(message[3]))
        s2.write(num2,column2+3,message[-5]+'  '+message[-4])
        num2=num2+1
        if num2==250:
            num2=0
            column2=column2+6

wb.save('takar hishab.xls')
