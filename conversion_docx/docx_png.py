import aspose.words as aw
import os
# load document
def docx_png_convert(a):
    doc = aw.Document(a)

    # set output image format
    options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)


    b = os.path.splitext(a)
    docx_doc= b[0]


    # loop through pages and convert them to PNG images

    ans=0
    for pageNumber in range(doc.page_count):
        options.page_set = aw.saving.PageSet(pageNumber)
        doc.save(docx_doc+str(pageNumber+1)+".png", options)
        ans=pageNumber+1
    return ans
        
