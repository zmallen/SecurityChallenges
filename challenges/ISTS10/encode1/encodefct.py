#!/usr/bin/env python

import string
import math
import base64
import htmllib

alphabet="z+]&WmOo3FjXb,4pkT=1I-$!w^?{tfR9D(S*B;>}dUYl<nPr)2N%ie/0ha6KECg:vZyJ875LsGqH.uM_\"VQ[#Acx@"
	
def encAscii(base, str):
	ret = ""
	alpha = alphabet
	for c in str:
		ret += alpha[ord(c) % base]
	return ret
	
def decAscii(str):
	ret = ""
	alpha = alphabet
	for c in str:
		index = alphabet.index(c)
		if index <= 32:
			index = index + 89
		ret += chr(index)
	return ret
		
str = "0hHell0Th3r3!Th4nkYou4Att3ndingISTS10!ItIsGr3472HaveYouH3re.AsYouC4/\/Se3;An3nc0dingFun<7ion0nlyR3quiresABaseAndAnAlphab3tOfUrCh00sing!W3Hum4nZUseInt3g32sWi7hP0w3rs0fTw0ForOu2B4sesT0HeLpEnc0deND3cod3B1t5OfInformationONOurComput3r5inAPr3c1seAndF4stM4nn3r.ButYouCanChooseAnythingToBeYourAlphabet!ForMine,IUs3dAR4nd0mlyG3n3ratedAlph4b3tOfUn1QU3L3tters4ndAR4ndo0B4seWithRandomSequence0fCh4r4cters!3nc0d1ng4lph4betsMu5tB3uNiQu3aNdn0nR3p34t1ngOrY0uW1llG3tSom3FunkyR3su1t5!D1dY0u4dd32AsAn0ffsetF0rTheAsc11D3c0d3rSoY0uc4nG3tPr1nt4bl3Ch4r4ct3rs?IHopeSo!FindT3chyAndMutt3rSyndaR1nElvishW0rdForFriendForS0mePointsForY0urTeam!"

base89 = encAscii(len(alphabet), str)

Base64 = base64.b64encode(base89)

print Base64

## HOW TO DECODE ##
Base64Dec = base64.b64decode(Base64)

decoded = decAscii(Base64Dec)
print "\n\n"
print decoded

######
