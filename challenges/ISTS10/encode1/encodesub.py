#!/usr/bin/env python

# base_34, base_55, base_89
import string
import math

alphabet="z+]&WmOo3FjXb,4pkT=1I-$!w^?{tfR9D(S*B;>}dUYl<nPr)2N%ie/0ha6KECg:vZyJ875LsGqH.uM_\"VQ[#Acx@"
base55alpha = alphabet[:55]


str = "OhHelloThere!"

# encode to base 89 from ASCII

base89 = ""
for c in str:
	base89 += alphabet[ord(c) % 89]
print base89

# encode to base 55 from base 89

base55 = ""
for c in base89:
	base55 += base55alpha[alphabet.index(c) % 55]
print base55

toBase89 = ""
for c in base55:
	index = base55alpha.index(c)
	toBase89 += base55alpha[index]
print toBase89

# works!
# decode from base 89 to ASCII

strdec = ""
for c in base89:
	index = alphabet.index(c)
	if index <= 32:
		index = index + 89
	fin = chr(index)
	strdec += fin

print strdec
print ord('~')