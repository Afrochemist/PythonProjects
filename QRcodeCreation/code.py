#This qr code will provide a link to aol

import qrcode

#function to make a qr code
img = qrcode.make ("aol.com")

#producing and saving the qr code
img.save("aol.png")
