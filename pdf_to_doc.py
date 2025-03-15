from pdf2docx import Converter

pdf_file = 'B:\PDF\水井湾风电场电力监控系统安全防护评估报告2021.11.24.pdf'
docx_file = 'B:\DOC\水井湾风电场电力监控系统安全防护评估报告2021.11.24.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()