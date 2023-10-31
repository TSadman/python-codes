file=input('Enter file name: ')
file=file+'.txt'
handle=open(file)
count=dict()
w_count=0
for line in handle:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
        if count[word]==1:
            w_count=w_count+1
print('Total words:',w_count)
m_value=None
m_key=None
for key,value in count.items():
    if m_key==None or m_value<value:
        m_key=key
        m_value=value
print('max value: {}'.format(m_value))
while True:                         #calculate how many times i have the values
    x=0
    want=input('Enter how many times you want the number: ') #@
    if want=='done': break
    wanted=want
    #try:
    #    wated=int(want)
    #except:
    #    print('Invalid input')
    #    continue
    #wanted=int(want)
    for key in count.keys():
        if wanted in key:
            x=x+1
    print('Your word count of {} is here {} times'.format(wanted,x))
w_want=dict()
for key,value in count.items():
    if wanted in key:
        w_want[key]=value
print(want,wanted)
for k,v in w_want.items():
    print(k,':',v)
if w_want=={}:
    print('No words were found!')
