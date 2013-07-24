#!/bin/bash

for line in `cat ists10real.txt`
do
	echo "<br>$line" >> tohtml.txt
done
