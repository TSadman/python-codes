import xlrd

file=xlrd.open_workbook("Newton-cotes.xlsx")
sheet=file.sheet_by_index(0)

x=list()
y=list()
area=0

for ii in range (1,sheet.nrows):
    x.append(sheet.cell_value(ii, 0))
    y.append(sheet.cell_value(ii, 1))

for jj in range(int((len(x)-1)/2)):
    area=area+(x[jj+1]-x[jj])*(y[jj]+y[jj+1])/2

print(area)
