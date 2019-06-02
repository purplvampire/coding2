import PyPDF2
# Open PDF and Create PDF Object
pdf1File = open('meetingminutes.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# Create a new PDF Object
pdfWriter = PyPDF2.PdfFileWriter()

# Combine 2 PDF File
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Create PDF File
pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

# Close File
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()