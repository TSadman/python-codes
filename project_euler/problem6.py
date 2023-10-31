num=100
sq_sum=0
wh_sum=0
for ii in range(100):
    sq_sum=sq_sum+(ii+1)**2
    wh_sum=wh_sum+(ii+1)
print(wh_sum**2-sq_sum)
