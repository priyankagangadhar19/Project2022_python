import openpyxl

#open the excel file-workbook
try:
    wb=openpyxl.load_workbook('F:/B64/Book2.xlsx')
    v=wb['Sheet1'].cell(1,1).value
    print(v)
    wb.close()
except Exception as e:
    print(e)
    print('Sorry something is wrong,ply try later')