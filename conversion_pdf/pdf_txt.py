import PyPDF2
import os


def pdf_txt_convert(a):
    pdfFileObject=open(a,'rb')
    
    b = os.path.splitext(a)
    pdf_txt = b[0] + ".txt"
    pdfReader=PyPDF2.PdfFileReader(pdfFileObject)
    
    pageObject=pdfReader.getPage(0)
    
    text= pageObject.extractText()
    pdfFileObject.close
    
    with open(pdf_txt,'w') as file:
        file.writelines(text)