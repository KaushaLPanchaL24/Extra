from pypdf import PdfMerger

pdf_files = [
    "file1.pdf",
    "file2.pdf",
    "file3.pdf"
]

output_pdf = "merged_output.pdf"

merger = PdfMerger()

for pdf in pdf_files:
    merger.append(pdf)

merger.write(output_pdf)
merger.close()

print("PDFs merged successfully!")
