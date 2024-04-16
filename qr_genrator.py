# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:54:04 2024

@author: bhara
"""

# import modules
import qrcode
from PIL import Image


def qrcode_generator(url):
    # taking image which user wants 
    # in the QR code center
    Logo_link = 'image-copy.jpg'

    logo = Image.open(Logo_link)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
    	error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # adding URL or text to QRcode
    QRcode.add_data(url)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = 'Black'

    # adding color to QR code
    QRimg = QRcode.make_image(
    	fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
    	(QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    
    filename = url.split('/')[4].split('?')[0].replace('-', '_') + '.png';
    
    print(filename)
    # save the QR code generated
    QRimg.save(filename)

    print('QR code generated!')


# taking url or text
# list of urls whose qr code needs to be generaeted
url_array = [   
]

for url in url_array:
    qrcode_generator(url)


