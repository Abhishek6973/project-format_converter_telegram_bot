import docx2txt
import os

def docx_txt_convert(a):
# Example file:
    docxFilename = a
    
    b = os.path.splitext(a)
    docx_txt= b[0] + ".txt"
    
    MY_TEXT = docx2txt.process(a)
    # print(MY_TEXT)
    
    with open(docx_txt, "w") as text_file:
        text_file.writelines(MY_TEXT)
    