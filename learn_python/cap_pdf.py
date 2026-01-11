from PyPDF2 import PdfWriter

pdfs = []

while (pdf_path := input("Please provide pdf path to be merged or type \"done\" if you are done\n")) != "done":
    pdfs.append(pdf_path)

pdfMerger = PdfWriter()
for pdf in pdfs:
    pdfMerger.append(pdf)

pdfMerger.write("merged-pdfs.pdf")
pdfMerger.close()

print(f"pdfs={pdfs} have been merged into one pdf \"merged-pdf.pdf\"")

