import qrcode
import Image
img = qrcode.make('j\'aime jess')
img.save("/Users/techy/projects/ISTS10/stego2/test", "JPEG")
