import Image
import qrcode
import os

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data('1f793b027d30200b3a122e68087523011a7c34693f7d0020197622231f102b307e312e75233f3b12327a2a3025762d27634d2a7a202328357a3c2456763b2a753e04030a0568050808110e0e170a1669')
qr.make(fit=True)
x = qr.make_image()
x.save("woot.jpg")
