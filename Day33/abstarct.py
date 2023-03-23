import openpyxl

#open the excel file-workbook
wb=openpyxl.load_workbook('F:/B64/Book1.xlsx')
for i in range(1,5):
    for j in range(1,4):
        v=wb['Sheet2'].cell(i,j).value
        print(v,end=' ')
    print()

wb.close()