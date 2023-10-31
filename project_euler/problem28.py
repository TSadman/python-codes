square_mat=list()
mat=6

for num in range(mat+2):
    temp_mat=list()
    for inner in range(mat+2):
        temp_mat.append(0)
    square_mat.append(temp_mat)

row=int(mat/2+1)
col=int(mat/2+1)

for num in range(1,mat*mat+1):
    square_mat[row][col]=num
    if square_mat[row][col+1]==0 and square_mat[row+1][col]==0 and square_mat[row][col-1]==0 and square_mat[row-1][col]==0:
        col=col+1
    elif square_mat[row][col+1]==0 and square_mat[row+1][col]==0 and square_mat[row][col-1]!=0 and square_mat[row-1][col]==0:
        row=row+1
    elif square_mat[row][col+1]==0 and square_mat[row+1][col]==0 and square_mat[row][col-1]==0 and square_mat[row-1][col]!=0:
        col=col-1
    elif square_mat[row][col+1]!=0 and square_mat[row+1][col]==0 and square_mat[row][col-1]==0 and square_mat[row-1][col]!=0:
        col=col-1
    elif square_mat[row][col+1]!=0 and square_mat[row+1][col]==0 and square_mat[row][col-1]==0 and square_mat[row-1][col]==0:
        row=row-1
    elif square_mat[row][col+1]!=0 and square_mat[row+1][col]!=0 and square_mat[row][col-1]==0 and square_mat[row-1][col]==0:
        row=row-1
    elif square_mat[row][col+1]==0 and square_mat[row+1][col]!=0 and square_mat[row][col-1]==0 and square_mat[row-1][col]==0:
        col=col+1
    elif square_mat[row][col+1]==0 and square_mat[row+1][col]!=0 and square_mat[row][col-1]!=0 and square_mat[row-1][col]==0:
        col=col+1
    #elif square_mat[row][col+1]==0 and square_mat[row+1][col]==0 and square_mat[row][col-1]!=0 and square_mat[row-1][col]==0:
     #   row=row+1
    elif square_mat[row][col+1]==0 and square_mat[row+1][col]==0 and square_mat[row][col-1]!=0 and square_mat[row-1][col]!=0:
        row=row+1
    
for row in range(1,mat+1):
    for col in range(1,mat+1):
        print("{0:3d}".format(square_mat[row][col]),end='')
    print('\n')

sum=0

for ii in range(1,mat+1):
    sum=sum+(square_mat[ii][ii]+square_mat[ii][mat+1-ii])
    
print('sum:',sum-1)