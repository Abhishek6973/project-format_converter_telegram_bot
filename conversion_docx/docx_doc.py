import docx
import os


def docx_doc_convert(a):
    b = os.path.splitext(a)
    docx_doc= b[0] + ".doc"

    doc = docx.Document(a)
    
    doc.save(docx_doc)
    