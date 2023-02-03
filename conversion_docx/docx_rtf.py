from docx import Document
import os

def docx_rtf_convert(a):
    f = open(a, 'rb')
    document = Document(f)

    b=os.path.splitext(a)
    file_name=b[0]+'.rtf'
    
    document.save(file_name)

