import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

count=4#int(input('Enter count:'))
pos=3#int(input('Enter position:'))
url=input('Enter:-')

for ii in range(count):#mane ei koyta page e jabe
    html=urllib.request.urlopen(url,context=ctx).read()#amra je page chacchi, oita load kore
    soup=BeautifulSoup(html,'html.parser')#oi page guchay
    jj=1
    #print(soup)
    tags = soup('a')
    print(tags)
    for tag in tags:#tags list er shobgula ekta ekta kore check kore
        if jj==pos:#desired number e gele active hoy
            print(tag.contents[0])#prints name
            url=tag.get('href',None)#returns the url associated with the name
        jj+=1
