import aspose.words as aw
import os

def pdf_rtf_convert(a):
    
    b = os.path.splitext(a)
    file_name = b[0] + ".rtf"
    rtf = aw.Document(a)
    rtf.save(file_name)
    
# from pdfminer.converter import TextConverter
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfpage import PDFPage
# import os

# def pdf_rtf_convert(path):
    
#     resource_manager = PDFResourceManager()
#     file = open(path.replace('.pdf', '.rtf'), 'w')
#     converter = TextConverter(resource_manager, file)
#     page_interpreter = PDFPageInterpreter(resource_manager, converter)
#     with open(path, 'rb') as fh:
#         for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
#             page_interpreter.process_page(page)
#     converter.close()
#     file.close()
