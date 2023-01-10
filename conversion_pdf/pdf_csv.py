import tabula 
import os
import imp

def pdf_csv_convert(a):
    b = os.path.splitext(a)
    pdf_csv = b[0] + ".csv"
    tabula.convert_into(a,pdf_csv, output_format="csv", pages='all')
    return pdf_csv

# if __name__ =="__main__":
    
#     main()
    
    