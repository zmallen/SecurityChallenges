#!/bin/bash
for line in `cat hexists`
do
	hmac=`echo -n $line | openssl dgst -md5 -hmac "tigers" | cut -d " " -f 2`
	echo "$line,$hmac" >> "realists.txt"
done
