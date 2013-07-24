#!/usr/bin/env python

# base_2, base_3, base_5, base_8, base_13, base_21, base_34, base_55, base_89
# with this my alphabet
import string
import math

alphabet="z+]&WmOo3FjXb,4pkT=1I-$!w^?{tfR9D(S*B;>}dUYl<nPr)2N%ie/0ha6KECg:vZyJ875LsGqH.uM_\"VQ[#Acx@"


base55alpha = alphabet[:55]
base34alpha = alphabet[:34]
base21alpha = alphabet[:21]
base13alpha = alphabet[:13]
base8alpha = alphabet[:8]
base5alpha = alphabet[:5]
base3alpha = alphabet[:3]
base2alpha = alphabet[:2]

str1 = "OhHelloThere!ThankYouForAttendingISTS10!ItIsGreatToHaveYouHere.AsYouCanSee,AnEncodingFunctionOnlyRequiresABaseAndAnAlphabetOfYourChoosing!WeHumansUseIntegersForOurBasesToHelpEncodeAndDecodeBitsOfInformationOnOurComputersinAPreciseAndFastManner.ButYouCanChooseAnythingToBeYourAlphabet!ForMine,IUsedASubsetOfTheFibonnacciSequenceForMyBasesAndARandomlyGeneratedAlphabetOfUniqueLettersForMyAlphabet!EncodingAlphabetsMustBeUniqueOrYouWillGetSomeFunkyResults.ToMakeLifeEasy,TheLastDecodeRequiresAsciiSoYouCanReadMyMessage!DidYouAdd32AsAnOffsetForTheAsciiDecoder?IHopeSo!FindTechyAndMutterTheLordOfTheRingsElvishWordForFriendForSomePointsForYourTeam!"

str = "ZackAllen!"

# encode

base89 = ""
for c in str:
	base89 += alphabet[ord(c) % 89]
print base89

base55 = ""
for c in base89:
	base55 += base55alpha[alphabet.index(c) % 55]
print base55

base34 = ""
for c in base55:
	base34 += base34alpha[alphabet.index(c) % 34]
	
#print base34

base21 = ""
for c in base34:
	base21 += base21alpha[alphabet.index(c) % 21]
	
#print base21

base13 = ""
for c in base21:
	base13 += base13alpha[alphabet.index(c) % 13]
	
#print base13

base8 = ""
for c in base13:
	base8 += base8alpha[alphabet.index(c) % 8]
#print base8


base5 = ""
for c in base8:
	base5 += base5alpha[alphabet.index(c) % 5]
#print base5

base3 = ""
for c in base5:
	base3 += base3alpha[alphabet.index(c) % 3]
#print base3

base2 = ""
for c in base3:
	base2 += base2alpha[alphabet.index(c) % 2]
#print base2


#######

nbase89 = ""
#print base55
for c in base55:
	print "c: " , c
	index = base55alpha.index(c)
	if index >= 34:
		index = index - 34
	print "index: " , index
	nbase89 += alphabet[index]
	print "\n"
print nbase89
#
#print base55Dec

strdec = ""
for c in base89:
	index = alphabet.index(c)
	if index <= 32:
		index = index + 89
	fin = chr(index)
	strdec += fin

print strdec