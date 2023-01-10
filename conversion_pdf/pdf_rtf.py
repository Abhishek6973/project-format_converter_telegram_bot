import aspose.words as aw
import os

def pdf_rtf_convert(a):
    
    b = os.path.splitext(a)
    file_name = b[0] + ".rtf"
    rtf = aw.Document(a)
    rtf.save(file_name)