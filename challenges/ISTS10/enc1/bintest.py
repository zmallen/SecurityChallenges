import Image
import qrcode
import os
from itertools import izip, cycle

# returns str xor'd with key byte by byte
def xor(str, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(str, cycle(key)))

	
plaintext = "Y0uF0unDm3h!F1nDT3cHy4NdT3llH1my0uc0mpl3t3dth3ch4ll3ngep4ssw0rd1sAMERICAFUCKYEAH"
key = "FINDMENOW!"

encText = ""

for i in range(1, (len(plaintext)/10)+1):
	substr = plaintext[(i-1)*10:(i*10)]
	encText += xor(substr, key)
encTextHex = encText.encode("hex")
print encTextHex

#decHex = encTextHex.decode("hex")

intext = "1f793b027d30200b3a122e68087523011a7c34693f7d0020197622231f102b307e312e75233f3b12327a2a3025762d27634d2a7a202328357a3c2456763b2a753e04030a0568050808110e0e170a1669"

decHex = intext.decode("hex")

decText = ""
for i in range(1, (len(decHex)/10)+1):
	substr = plaintext[(i-1)*10:(i*10)]
	decText += substr

print decText