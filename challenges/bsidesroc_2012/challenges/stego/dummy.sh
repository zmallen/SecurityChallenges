#!/bin/bash

for (( i=1; i<=50; i++ ))
do
	dumhex=`cat /dev/urandom | tr -cd 'A-F0-9' | head -c 10`
	hash=`echo $dumhex | openssl dgst -md5 -hmac "$dumhex" | cut -d " " -f 2`
	echo "$dumhex,$hash" >> stego.txt
done
