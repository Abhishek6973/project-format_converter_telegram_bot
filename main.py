import csv
from email import message
from fileinput import filename

from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton

import telebot
import os
import io

import random
import string
from pathlib import Path


from conversion_pdf import pdf_docx,pdf_mp3,pdf_csv,pdf_jpg,pdf_txt,pdf_png,pdf_rtf
from conversion_docx import docx_mp3, docx_pdf,docx_txt,docx_doc,docx_jpg,docx_png,docx_rtf
from conversion_jpg import jpg_pdf,jpg_gif,jpg_png
from conversion_png import png_jpg,png_gif,png_pdf


import PyPDF2




token = '5504002265:AAHRJ5aNWsmY-FInF6mBOcgouCu7_mrvPYk'
bot1 = Bot(token)

dp = Dispatcher(bot1)
token="5504002265:AAHRJ5aNWsmY-FInF6mBOcgouCu7_mrvPYk"

bot = telebot.TeleBot(token)


##################################### PDF HANDLER ###########################################


button1=InlineKeyboardButton(text="docx",callback_data="docx")
button2=InlineKeyboardButton(text="mp3",callback_data="mp3")
button3=InlineKeyboardButton(text="csv",callback_data="csv")
button4=InlineKeyboardButton(text="txt",callback_data="txt")
button5=InlineKeyboardButton(text="png",callback_data="png")
button6=InlineKeyboardButton(text="jpg",callback_data="jpg")
button7=InlineKeyboardButton(text="rtf",callback_data="rtf")


keyboard_inline_pdf = InlineKeyboardMarkup().add(button1,button2,button3).add(button4,button5,button6).add(button7)


##################################### DOCX HANDLER ###########################################


button8=InlineKeyboardButton(text="pdf",callback_data="docx_pdf")
button9=InlineKeyboardButton(text="mp3",callback_data="docx_mp3")
button10=InlineKeyboardButton(text="doc",callback_data="docx_doc")
button11=InlineKeyboardButton(text="txt",callback_data="docx_txt")
button12=InlineKeyboardButton(text="png",callback_data="docx_png")
button13=InlineKeyboardButton(text="jpg",callback_data="docx_jpg")
button14=InlineKeyboardButton(text="rtf",callback_data="docx_rtf")

keyboard_inline_docx = InlineKeyboardMarkup().add(button8,button9,button10).add(button11,button12,button13).add(button14)


##################################### JPG HANDLER #################################################


button15=InlineKeyboardButton(text="gif",callback_data="jpg_gif")
button16=InlineKeyboardButton(text="pdf",callback_data="jpg_pdf")
button17=InlineKeyboardButton(text="png",callback_data="jpg_png")

keyboard_inline_jpg = InlineKeyboardMarkup().add(button15,button16).add(button17)


##################################### PNG HANDLER ################################################


button18=InlineKeyboardButton(text="gif",callback_data="png_gif")
button19=InlineKeyboardButton(text="pdf",callback_data="png_pdf")
button20=InlineKeyboardButton(text="jpg",callback_data="png_jpg")

keyboard_inline_png = InlineKeyboardMarkup().add(button18,button19).add(button20)


global message1

global message2

message2=0

message1=0


##################################### Start Message HANDLER ###########################################


@dp.message_handler(commands=['start'])
async def send_welcome(message):

    start_message="""
    Hi! File Converter is at your service!
📷 Images,🔊 Audio,📹 Video and 
other files are supported.
Send me a file to convert or type
/help for more information."""

    bot.send_message(message.chat.id, start_message)

@dp.message_handler(commands=["aman"])
async def amn(message):
    bot.send_message(message.chat.id,"aman is also called chaman")


##################################### About Message HANDLER ###########################################

@dp.message_handler(commands=['about'])
async def about_messages(message):

    about_message="""🤖 Bot
Name: Testing_bot
Username: @test_201007_bot
Version: 3.5.1
Changelog: AIOGRAM(https://pypi.org/project/aiogram/),
TELEBOT(https://pypi.org/project/pyTelegramBotAPI/)
👤 Developer
Name: ABHISHEK KUMAR
Username: @Mohit0kr
Email: abhishek86649@gmail.com"""
    bot.send_message(message.chat.id, about_message)


##################################### Help Message HANDLER ###########################################


@dp.message_handler(commands=['help'])
async def help_messages(message):
    help_message="""Send me a file to convert.
12 Supported files:
📷 Images (4)
PNG, JPG, JPEG, GIF
🔊 Audio (1)
MP3
💼 Document (7)
TXT, DOC, DOCX, PDF, CSV, RTF, DOC
🙏PLEASE MAKE 😊PATINCE WE WILL ADD MORE FEATURES🎉"""
    bot.send_message(message.chat.id,help_message)


##################################### Support Message HANDLER ###########################################



@dp.message_handler(commands = ['support'])
async def support_message(message):

    support_messages="""Hey please support us😊! 
your support inspire us for making incredible design💰."""

    bot.send_message(message.chat.id,support_messages)

    payment_info="""USDT-TRC20(Spot wallet) => TLTbJaGGjMcWAgsG9wWvDjKYwWDgUEMY8o 
    
USDR-BEP20(Spot wallet) => xc4e20a8a8c130a65b15f581b7f1a9dd11f0f7522"""

    bot.send_message(message.chat.id,payment_info)


##################################### DOCUMENT HANDLER ###########################################


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def random_answer(message:types.Message):
    global message1
    message1=message
    message2=message

    file_name = message.document.file_name
    extension= file_name.split('.')[1]

    if extension=='pdf':
        await message.reply("Available conversion that we support for pdf..",reply_markup=keyboard_inline_pdf)

    if extension=='docx':
         await message.reply("Available conversion that we support for docx..",reply_markup=keyboard_inline_docx)

    if extension=='png':

        await message.reply("Available conversion that we support for png..",reply_markup=keyboard_inline_png)


#################################### IMAGE HANDLER ###########################################


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def random_answer(message:types.Message):
    global message2
    message2=message

    await message2.reply("Available conversion that we support for jpg..",reply_markup=keyboard_inline_jpg)

##################################### IMAGE HANDLER ###########################################


global main_pic_name
main_pic_name=""
@dp.callback_query_handler(text=["jpg_gif","jpg_png","jpg_pdf"])
async def random_value(call:types.CallbackQuery):
    global pic_counter


######################################### IMAGE JPG_GIF HANDLER ###########################################

    try:           
        if call.data=='jpg_gif':
            await call.message.reply("available for conversion")


            file = await message2.photo[-1].get_file()

            file_name_len=12
            res = ''.join(random.choices(string.ascii_uppercase +
                                        string.digits, k=file_name_len))
            file_name=str(res)+'.jpg'

            await file.download(file_name)

            bot.reply_to(message2,"Gif conversion in process⌛...")

            try:
                jpg_gif.jpg_gif_convert(file_name)

                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message2.chat.id, document=open(f'{get_name_without_extension}.gif', 'rb'))

            except:
                error_message = """ℹ️ Task Details
    Conversion: JPG ➡ GIF
    Status: Failed
    ❌ Conversion failed
    Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.gif')


########################################## IMAGE JPG_PNG HANDLER ###########################################


        elif call.data=='jpg_png':
            # await call.message.reply("available for conversion")        

            file = await message2.photo[-1].get_file()

            file_name_len=12
            res = ''.join(random.choices(string.ascii_uppercase +
                                        string.digits, k=file_name_len))
            file_name=str(res)+'.jpg'

            await file.download(file_name)

            bot.reply_to(message2,"png conversion in process⌛")

            try:
                jpg_png.jpg_png_convert(file_name)

                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message2.chat.id, document=open(f'{get_name_without_extension}.png', 'rb'))

            except:
                error_message = """ℹ️ Task Details
    Conversion: JPG ➡ PNG
    Status: Failed
    ❌ Conversion failed
    Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.png')


######################################### IMAGE JPG_PDF HANDLER ###########################################


        elif call.data == 'jpg_pdf':

            file = await message2.photo[-1].get_file()

            file_name_len=12
            res = ''.join(random.choices(string.ascii_uppercase +
                                        string.digits, k=file_name_len))
            file_name=str(res)+'.jpg'

            await file.download(file_name)

            bot.reply_to(message2,"pdf conversion in process⌛..")

            jpg_pdf.jpg_pdf_convert(file_name)

            try:
                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message2.chat.id, document=open(f'{get_name_without_extension}.pdf', 'rb'))

            except:
                error_message = """ℹ️ Task Details
    Conversion: JPG ➡ PDF
    Status: Failed
    ❌ Conversion failed
    Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.pdf')

    except Exception as e:
        error_message = "An error occurred: "
        bot.reply_to(message1, error_message)


##################################### IMAGE PNG HANDLER ###########################################


@dp.callback_query_handler(text=["png_gif","png_jpg","png_pdf"])
async def random_value(call:types.CallbackQuery):


 ######################################### IMAGE PNG_GIF HANDLER ###########################################

    try:
        if call.data=='png_gif':
            await call.message.reply("available for conversion")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pngtogif = bot.get_file(file_id)
            downloaded_file = bot.download_file(pngtogif.file_path)


            bot.reply_to(message1,"gif conversion in process⌛...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            try:
                png_gif.png_gif_convert(file_name)    

                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.gif', 'rb'))

            except:
                error_message = """ℹ️ Task Details
Conversion: PNG ➡ GIF
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:  
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.gif')


######################################### IMAGE PNG_JPG HANDLER ###########################################


        elif call.data=='png_jpg':
            await call.message.reply("available for conversion")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pngtojpg = bot.get_file(file_id)
            downloaded_file = bot.download_file(pngtojpg.file_path)

            bot.reply_to(message1,"jpg conversion in process⌛...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            try:
                png_jpg.png_jpg_convert(file_name)

                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.jpg', 'rb'))

            except:    
                error_message = """ℹ️ Task Details
Conversion: PNG ➡ JPG
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:   
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.jpg')


 ######################################### IMAGE PNG_PDF HANDLER ###########################################


        elif call.data=='png_pdf':
            await call.message.reply("available for conversion")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pngtopdf = bot.get_file(file_id)
            downloaded_file = bot.download_file(pngtopdf.file_path)

            bot.reply_to(message1,"pdf conversion in process⌛...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            try:
                png_pdf.png_pdf_convert(file_name)

                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.pdf', 'rb'))
            except:
                error_message = """ℹ️ Task Details
Conversion: PNG ➡ PDF
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.pdf')

    except Exception as e:
        error_message = "An error occurred: "
        bot.reply_to(message1, error_message)


##################################### DOCUMENT PDF HANDLER ###########################################


@dp.callback_query_handler(text=["docx","mp3","csv","txt","png","jpg","rtf"])
async def random_value(call:types.CallbackQuery):

 ##################################### DOCUMENT PDF TO DOCX HANDLER ###########################################

    try:
        if call.data=="docx":
            global message1
            await call.message.reply("available for conversion")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"docx conversion in process...⌛")

            try:
                with open(f'{file_name}', 'wb') as file:
                    file.write(downloaded_file)

                docx_file=pdf_docx.pdf_docx_convert(file_name)

                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.docx', 'rb'))

            except:
                error_message = """ℹ️ Task Details
Conversion: PDF ➡ DOCX
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
            # path_name=os.path(filename)
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.docx')


##################################### DOCUMENT PDF TO MP3 HANDLER ###########################################


        elif call.data=="mp3":
            await call.message.reply("available for conversion")  
            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"mp3 conversion in process...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            try:
                bot.send_message(message1.chat.id, "File converting is started,please wait⌛\n")
                get_name_without_extension = file_name.split('.')[0]

                result = pdf_mp3.pdf_to_mp3(file_path=f'{get_name_without_extension}.pdf', language="en")

                bot.send_message(message1.chat.id, result)
                bot.send_audio(chat_id=message1.chat.id, audio=open(f'{get_name_without_extension}.mp3', 'rb'))

            except:
                error_message = """ℹ️ Task Details
Conversion: PDF ➡ MP3
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.mp3')


##################################### DOCUMENT PDF TO CSV HANDLER ###########################################


        elif call.data=="csv":
            await call.message.reply("available for conversion..")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"csv conversion in process...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            bot.send_message(message1.chat.id, "File converting is started,please wait ⌛\n")
            get_name_without_extension = file_name.split('.')[0]

            try:
                csv_file=pdf_csv.pdf_csv_convert(file_name)

                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.csv', 'rb'))

            except Exception as conversion_error:
                error_message = """ℹ️ Task Details
Conversion: PDF ➡ CSV
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.csv')

##################################### DOCUMENT PDF TO TXT HANDLER ###########################################


        elif call.data=="txt":
            await call.message.reply("available for conversion..")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"txt conversion in process...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            bot.send_message(message1.chat.id, "File converting is started, Please Wait⌛\n")

            try:
                pdf_txt.pdf_txt_convert(file_name)
                get_name_without_extension = file_name.split('.')[0]
                bot.send_document(chat_id=message1.chat.id, document=open(f'{get_name_without_extension}.txt', 'rb'))

            except Exception as conversion_error:
                error_message = """ℹ️ Task Details
Conversion: PDF ➡ TXT
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))  # Remove the downloaded PDF file
                os.remove(f'{get_name_without_extension}.txt') 


##################################### DOCUMENT PDF TO PNG HANDLER ###########################################


        elif call.data=="png":
            await call.message.reply(" available for conversion..")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"png conversion in process...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            bot.send_message(message1.chat.id, "File converting is started,please wait⌛\n")
            get_name_without_extension = file_name.split('.')[0]

            try:
                png_file=pdf_png.pdf_png_convert(file_name)

                file = open(file_name, 'rb')
                readpdf = PyPDF2.PdfFileReader(file)
                totalpages = readpdf.numPages

                for i in range(totalpages):
                    bot.send_document(chat_id = message1.chat.id, document=open(get_name_without_extension+str(i)+'.png', 'rb'))

            except Exception as conversion_error:
                error_message = """ℹ️ Task Details
Conversion: PDF ➡ PNG
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))

                for i in range(totalpages):
                    os.remove(str(get_name_without_extension)+str(i)+'.png')


##################################### DOCUMENT PDF TO JPG HANDLER ###########################################


        elif call.data=="jpg":
            await call.message.reply(" available for conversion..")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"jpg conversion in process...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            bot.send_message(message1.chat.id, "File converting is started,please wait⌛\n")

            get_name_without_extension = file_name.split('.')[0]

            try:
                png_file=pdf_jpg.pdf_jpg_convert(file_name)

                file = open(file_name, 'rb')
                readpdf = PyPDF2.PdfFileReader(file)
                totalpages = readpdf.numPages

                for i in range(totalpages):
                    bot.send_document(chat_id = message1.chat.id, document=open(get_name_without_extension+str(i)+'.jpg', 'rb'))

            except Exception as conversion_error:
                error_message = """ℹ️ Task Details
Conversion: PDF ➡ JPG
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))

                for i in range(totalpages):
                    os.remove(str(get_name_without_extension)+str(i)+'.jpg')


##################################### DOCUMENT PDF TO RTF HANDLER ###########################################


        elif call.data=="rtf":
            await call.message.reply(" available for conversion..")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"rtf conversion in process...")

            with open(f'{file_name}', 'wb') as file:
                file.write(downloaded_file)

            bot.send_message(message1.chat.id, "File converting is started,please wait⌛\n")

            get_name_without_extension = file_name.split('.')[0]

            try:
                png_file=pdf_rtf.pdf_rtf_convert(file_name)

                get_name_without_extension = file_name.split('.')[0]
                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.rtf', 'rb'))

            except Exception as conversion_error:
                error_message = """ℹ️ Task Details
Conversion: PDF ➡ RTF
Status: Failed
❌ Conversion failed
Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.rtf')

        await call.answer()

    except Exception as e:
        error_message = "An error occurred: "
        bot.reply_to(message1, error_message)



###################################### DOCUMENT DOCX HANDLER ###########################################


@dp.callback_query_handler(text=["docx_pdf","docx_mp3","docx_doc","docx_txt","docx_png","docx_jpg","docx_rtf"])
async def random_value(call:types.CallbackQuery):


##################################### DOCUMENT DOCX TO PDF HANDLER ###########################################


    try:
        if call.data=="docx_pdf":

            await call.message.reply("pdf available for conversion")
            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"pdf conversion in process⌛...")

            try:
                with open(f'{file_name}', 'wb') as file:
                    file.write(downloaded_file)

                bot.send_message(message1.chat.id, "pdf converting is started,please wait⌛\n")

                get_name_without_extension = file_name.split('.')[0]
                pdf_file=docx_pdf.docx_pdf_convert(file_name)    

                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.pdf', 'rb'))

            except: 
                error_message = """ℹ️ Task Details
        Conversion: DOCX ➡ PDF
        Status: Failed
        ❌ Conversion failed
        Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.pdf')


##################################### DOCUMENT DOCX TO MP3 HANDLER ###########################################


        elif call.data=="docx_mp3":

            await call.message.reply("mp3 available for conversion.")
            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"mp3 conversion in process⌛...")

            try:
                with open(f'{file_name}', 'wb') as file:
                    file.write(downloaded_file)

                get_name_without_extension = file_name.split('.')[0]

                docx_mp3.docx_mp3_convert(file_path=f'{get_name_without_extension}.docx', language="en")

                bot.send_audio(chat_id=message1.chat.id, audio=open(f'{get_name_without_extension}.mp3', 'rb'))

            except: 
                error_message = """ℹ️ Task Details
            Conversion: DOCX ➡ MP3
            Status: Failed
            ❌ Conversion failed
            Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.mp3')


##################################### DOCUMENT DOCX TO CSV HANDLER ###########################################


        elif call.data=="docx_doc":

            await call.message.reply("doc available for conversion.")
            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"doc conversion in process⌛...")

            try:
                with open(f'{file_name}', 'wb') as file:
                    file.write(downloaded_file)

                get_name_without_extension = file_name.split('.')[0]
                doc_file=docx_doc.docx_doc_convert(file_name)


                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.doc', 'rb'))

            except:
                error_message = """ℹ️ Task Details
        Conversion: DOCX ➡ CSV
        Status: Failed
        ❌ Conversion failed
        Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:   
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.doc')


##################################### DOCUMENT DOCX TO TXT HANDLER ###########################################


        elif call.data=="docx_txt":

            await call.message.reply("txt available for conversion⌛...")
            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            try:
                bot.reply_to(message1,"txt conversion in process...")

                with open(f'{file_name}', 'wb') as file:
                    file.write(downloaded_file)

                get_name_without_extension = file_name.split('.')[0]
                txt_file=docx_txt.docx_txt_convert(file_name)

                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.txt', 'rb'))

            except:
                error_message = """ℹ️ Task Details
        Conversion: DOCX ➡ TXT
        Status: Failed
        ❌ Conversion failed
        Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(str(get_name_without_extension)+'.txt')


##################################### DOCUMENT DOCX TO PNG HANDLER ###########################################


        elif call.data=="docx_png":

            await call.message.reply(" available for conversion..")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"png conversion in process⌛...")

            try:
                with open(f'{file_name}', 'wb') as file:
                    file.write(downloaded_file)

                bot.send_message(message1.chat.id, "File converting is started,please wait\n")
                get_name_without_extension = file_name.split('.')[0]

                png_file=docx_png.docx_png_convert(file_name)

                for i in range(1,png_file+1):
                    bot.send_document(chat_id = message1.chat.id, document=open(get_name_without_extension+str(i)+'.png', 'rb'))

            except:
                error_message = """ℹ️ Task Details
        Conversion: DOCX ➡ PNG
        Status: Failed
        ❌ Conversion failed
        Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                for i in range(1,png_file+1):
                    os.remove(get_name_without_extension+str(i)+'.png')


##################################### DOCUMENT DOCX TO JPG HANDLER ###########################################


        elif call.data=="docx_jpg":

            await call.message.reply(" available for conversion..")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"jpg conversion in process⌛...")

            try:
                with open(f'{file_name}', 'wb') as file:
                    file.write(downloaded_file)

                docx_pdf.docx_pdf_convert(file_name)

                file_name = file_name.split('.')[0]
                file_name=file_name +'.pdf'

                pdf_jpg.pdf_jpg_convert(file_name)


                file = open(file_name, 'rb')
                readpdf = PyPDF2.PdfFileReader(file)
                totalpages = readpdf.numPages


                get_name_without_extension= file_name.split('.')[0]


                for i in range(totalpages):
                    bot.send_document(chat_id = message1.chat.id, document=open(get_name_without_extension+str(i)+'.jpg', 'rb'))

            except:
                error_message = """ℹ️ Task Details
        Conversion: DOCX ➡ JPG
        Status: Failed
        ❌ Conversion failed
        Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))

                for i in range(totalpages):
                    os.remove(get_name_without_extension+str(i)+'.jpg')


##################################### DOCUMENT DOCX TO RTF HANDLER ###########################################


        elif call.data=="docx_rtf":
            await call.message.reply(" available for conversion..")

            file_id = message1.document.file_id
            file_name = message1.document.file_name

            pdf_document = bot.get_file(file_id)
            downloaded_file = bot.download_file(pdf_document.file_path)

            bot.reply_to(message1,"rtf conversion in process⌛...")

            try:
                with open(f'{file_name}', 'wb') as file:
                    file.write(downloaded_file)

                docx_rtf.docx_rtf_convert(file_name)

                get_name_without_extension= file_name.split('.')[0]
                bot.send_document(chat_id = message1.chat.id, document=open(f'{get_name_without_extension}.rtf', 'rb'))

            except:
                error_message = """ℹ️ Task Details
        Conversion: DOCX ➡ RTF
        Status: Failed
        ❌ Conversion failed
        Error: Converted file is empty"""
                bot.reply_to(message1, error_message)

            finally:
                os.remove(str(file_name))
                os.remove(get_name_without_extension+'.rtf')

        await call.answer()

    except Exception as e:
        error_message = "An error occurred: "
        bot.reply_to(message1, error_message)




def main():
    executor.start_polling(dp)


if __name__=='__main__':
    main()