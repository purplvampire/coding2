#! python3
# Chart.py - Create Chat in Excel.
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
# Create some data in column A
for i in range(1, 11):
    sheet['A' + str(i)] = i
# First Source
refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
# First Series
seriesObj = openpyxl.chart.Series(refObj, title='First series')
# Create a Bar Chart
chartObj = openpyxl.chart.BarChart()
chartObj.title = 'My Chart'
chartObj.append(seriesObj)
# Append chart to sheet
sheet.add_chart(chartObj, 'C5')
# Save Excel
wb.save('sampleChart.xlsx')
