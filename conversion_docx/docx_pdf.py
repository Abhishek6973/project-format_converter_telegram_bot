import subprocess

def docx_pdf_convert(a):

    subprocess.call(['soffice',
                 # '--headless',
                 '--convert-to',
                 'pdf',
                 a])
    return a