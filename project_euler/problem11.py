handle=open('problem11.txt')
data=list()
data_lst=list()
for line in handle:
    data_lst=[]
    line=line.split()
    for numbers in line:
        data_lst.append(int(numbers))
    data.append(data_lst)

def vertical(r,c):
    return (data[r][c]*data[r+1][c]*data[r+2][c]*data[r+3][c])
def horizontal(r,c):
    return (data[r][c]*data[r][c+1]*data[r][c+2]*data[r][c+3])
def diag(r,c):
    return (data[r][c]*data[r+1][c+1]*data[r+2][c+2]*data[r+3][c+3])
def antidiag(r,c):
    return (data[r][c]*data[r+1][c-1]*data[r+2][c-2]*data[r+3][c-3])


col_max=len(data[0])
row_max=len(data)
maximum=1
for row in range(row_max):
    for col in range(col_max):
        chk_list=[]
        if row<=row_max-4:
            chk_mul=vertical(row,col)
            chk_list.append(chk_mul)
            print("vertical:",row+1, col+1, chk_mul)
        if col<=col_max-4:
            chk_mul=horizontal(row,col)
            chk_list.append(chk_mul)
            print("horizontal",row+1, col+1, chk_mul)
        if row<=row_max-4 and col<=col_max-4:
            chk_mul=diag(row,col)
            chk_list.append(chk_mul)
            print("diag",row+1, col+1, chk_mul)
        if row<=row_max-4 and col>=3:
            chk_mul=antidiag(row,col)
            chk_list.append(chk_mul)
            print("antidiag",row+1, col+1, chk_mul)
        else:
            chk_list.append(1)
        temp=max(chk_list)
        if temp>maximum:
            maximum=temp
        print(temp,"     ######     ",maximum)
        print("***************************************************")
print(maximum)
print(antidiag(0,3))
