def palindromic(num):
    num=str(num)
    if num==num[::-1]:
        return True
    else:
        return False
    
maximum=1000000
total=0

for decimal in range(1,maximum+1):
    binary=bin(decimal)
    binary=binary[2:]
    if palindromic(decimal) and palindromic(binary):
        print(decimal,binary)
        total=total+decimal
        
print(total)