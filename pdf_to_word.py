from pdf2docx import Converter

pdf_path = "Biodata.pdf"       # Your PDF file
docx_path = "output.docx"    # Output Word file

cv = Converter(pdf_path)
cv.convert(docx_path, start=0, end=None)
cv.close()

print("Conversion completed successfully!")
