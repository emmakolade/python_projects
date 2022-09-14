import qrcode


data = "subscribe"  # data to encode in to the qrcode

qr = qrcode.QRCode(version=1, box_size=20, border=10)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "blue", back_color = "white")
img.save("C:/Users/user/Desktop/Software Development/QRcode.png")

# img = qrcode.make(data)

# img.save("C:/Users/user/Documents/Pycharm/myqrcode.png")


#to get data from a QrCode

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/user/Desktop/Software Development/QRcode.png")

result = decode(img)

print(result)