name=input('Give me you name: ')
print('Your name is '+name)
age=input('Enter  your age: ')
print('Your age is '+age)
age=int(age)
year=2020
time=int(input('How many times: '))
for i in range(1,time+1):
    print('{}. The year you\'ll turn 100 is:'.format(i),year-age+100 )
def click():
    return 0
click()
