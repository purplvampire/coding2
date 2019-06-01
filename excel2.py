import openpyxl
wb = openpyxl.Workbook()
x = wb.get_sheet_names()
print(x)
# rename sheet
sheet = wb.active
sheet.title = 'Sapm Bacon Eggs Sheet'
x = wb.get_sheet_names()
print(x)
# create sheet
wb.create_sheet(index=0, title='First Sheet')
wb.create_sheet(index=2, title='Middle Sheet')
x = wb.get_sheet_names()
print(x)
# remove sheet
wb.remove_sheet(wb.get_sheet_by_name('First Sheet'))
wb.remove_sheet(wb.get_sheet_by_name('Middle Sheet'))
x = wb.get_sheet_names()
print(x)
# insert data to cell
sheet = wb.get_sheet_by_name('Sapm Bacon Eggs Sheet')
sheet['A1'] = 'Hello World!'
y = sheet['A1'].value
print(y)
# save file
wb.save('example_copy.xlsx')

