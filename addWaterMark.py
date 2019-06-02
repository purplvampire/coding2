import PyPDF2
# Create Pdf Object
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWartermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# Merge Warter Mark in Page 1 to New PDF
minutesFirstPage.mergePage(pdfWartermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)
# Append other page to New PDF
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
# Create PDF File and Encrypt
resultPdfFile = open('watermarkedCover2.pdf', 'wb')
pdfWriter.encrypt('1234')
pdfWriter.write(resultPdfFile)
# Close PDF File
resultPdfFile.close()
minutesFile.close()
