#!/bin/bash

#Write a shell script that takes pairs of parameters (a filename and a number 
#n) and outputs for each pair the name of the file, the number n and the nth 
#word from each file.

if [ $(($#%2)) -ne 0 ]; then
	# Check if there is an even number of parameters, so we have pairs.
	echo Please enter the parameters correctly.
	exit 1
fi

while [ $# -ne 0 ]
do
	# Parse through the parameter list
	echo $1
	echo $2
	var=`cat $1 | wc -w `
	# Get the number of words in the file
	if [ $var -lt $2 ] ; then
                echo Not enough words in file.
        else
		cat $1 | cut -d' ' -f$2
		# If ther eare enough words, print the nth one.
	fi	
	shift 2
done
