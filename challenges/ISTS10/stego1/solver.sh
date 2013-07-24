#!/bin/bash

for line in `cat testformsite.txt`
do
	val=`echo $line | cut -d "," -f 1`
	hash=`echo $line | cut -d "," -f 2`
	testhash=`echo -n $val | openssl dgst -md5 -hmac "tigers" | cut -d " " -f 2`
	if [ "$hash" = "$testhash" ]
	then
		echo "Hashes match!"
		
		echo "$val" | tr -d "\n" >> "solved.txt"
	else
		echo "Hashes do not match. Not authenticated"
	fi
done
