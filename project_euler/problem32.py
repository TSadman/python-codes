#We will store the products in a set to avoid duplicates
products = set()

#Digits from 1-9 which will be checking later
to_be_checked = set('123456789')

#for single digit multiplicand
for i in range(9):
	for j in range(1000,10000):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == to_be_checked:
			products.add(i*j)
		elif len(s) > 9:break

#for double digit multiplicand
for i in range(10,100):
	for j in range(100,1000):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == to_be_checked:
			products.add(i*j)
		elif len(s)>9: break

#printing the result
print(sum(products))
