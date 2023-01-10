from email import message
from lib2to3.pgen2 import token
import telebot
import os
# from private import token
from conversion_pdf import pdf_docx
import time

token="5504002265:AAHRJ5aNWsmY-FInF6mBOcgouCu7_mrvPYk"

# def tele_bot(token):
bot = telebot.TeleBot(token)
    
#     @bot.message_handler(commands=['start', 'help'])
#     def send_welcome(message):
# 	    bot.reply_to(message.chat.id, "Howdy, how are you doing?")
#         # print(message.message_id)

     
#     @bot.message_handler(func=lambda m: True)
#     def echo_all(message):
#         bot.reply_to(message, message.text)
        
@bot.message_handler(content_types=["document"])
def get_doc_and_convert(message):
    file_id = message.document.file_id
    file_name = message.document.file_name
    # asd=os.path.splitext(file_name)
    print(message)
    pdf_document = bot.get_file(file_id)
    downloaded_file = bot.download_file(pdf_document.file_path)
    bot.reply_to(message,"docx conversion in process...")
    with open(f'{file_name}', 'wb') as file:
        file.write(downloaded_file)
    docx_file=pdf_docx.pdf_docx_convert(file_name)
    get_name_without_extension= file_name.split('.')[0]
    bot.send_document(chat_id=message.chat.id, document=open(f'{get_name_without_extension}.docx', 'rb'))

while True:
    try:
        bot.polling(non_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(5)
        continue

    
    

# token="5504002265:AAHRJ5aNWsmY-FInF6mBOcgouCu7_mrvPYk"
# tele_bot(token)