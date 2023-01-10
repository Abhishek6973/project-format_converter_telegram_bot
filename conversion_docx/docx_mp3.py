from xml.dom.minidom import Document
import docx
from gtts import gTTS
from pathlib import Path

def docx_mp3_convert(file_path="test.pdf", language="en"):
    
    
    doc = docx.Document(file_path)
    fullText = []
    
    for para in doc.paragraphs:
        fullText.append(para.text)
        
    text = ''.join(fullText)
    text = text.replace('\n', '')
    
    print("conversion started..")
    
    my_audio = gTTS(text=text, lang=language, slow=False)
    
    file_name = Path(file_path).stem
    my_audio.save(f'{file_name}.mp3')
    
    
    print("file created ..")
    
