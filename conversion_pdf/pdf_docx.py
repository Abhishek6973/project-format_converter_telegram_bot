import imp
from pdf2docx import *
import os


def pdf_docx_convert(a):
    
    b = os.path.splitext(a)
    
    pdf_docxx = b[0] + ".docx"
    parse(a,pdf_docxx)
    
    return pdf_docxx

if __name__ =="__main__":
    
    main()
    
    
    




    