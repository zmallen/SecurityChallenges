#!/bin/bash

for line in `cat stego.txt`
do
	val=`echo $line | cut -d "," -f 1`
	hash=`echo $line | cut -d "," -f 2`
	testhash=`echo -n $val | openssl dgst -md5 -hmac "rochester" | cut -d " " -f 2`
	if [ "$hash" = "$testhash" ]
	then
		echo "Hashes match!"
		
		echo "$val" | tr -d "\n" >> "tosolve.txt"
	else
		echo "Hashes do not match. Not authenticated"
	fi
done
