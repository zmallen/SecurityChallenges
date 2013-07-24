#!/bin/bash
for line in `cat hex`
do
	hmac=`echo -n $line | openssl dgst -md5 -hmac "rochester" | cut -d " " -f 2`
	echo "$line,$hmac" >> "real.txt"
done
