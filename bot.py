import telebot
from PIL import Image
import numpy as np
import cv2
from rembg import remove

# Replace 'YOUR_BOT_TOKEN' with your bot token
BOT = telebot.TeleBot('7238717600:AAF2ReLPIxItfqltUsTJddCnqiJ10mH14kA')

@BOT.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = BOT.get_file(message.photo[-1].file_id)
    downloaded_file = BOT.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    img = Image.open('image.jpg')
    output = remove(img)

    output.save('output.png')

    BOT.send_photo(message.chat.id, open('output.png', 'rb'))

BOT.polling()
