#!/usr/bin/env python

import string
from random import sample
chars = string.letters + string.digits + '=-[];,./_+{}:"<>?!@#$%^&*()'
print len(string.letters)
print len(string.digits)
print len(chars)

length = 89
gen = ''.join(sample(chars, length))
print gen
length = 55
gen = ''.join(sample(chars, length))
print gen

length = 34
gen = ''.join(sample(chars, length))
print gen
