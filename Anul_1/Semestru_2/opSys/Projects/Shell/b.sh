#!/bin/bash

#Write a shell script that will create a file that contains a list of all the files 
#from a folder given in the command line and its subfolders, that have none 
#of the read, write and execute permission for the group.Then, for each file, 
#grant read permission to the group. 

if [ $# -ne 1 ]; then
	#Check for correct number of parameters.
	echo Enter parameters correctly, please
	exit 2
fi

cd $1 2> dump.txt 
# Try to access the directory, if not there, get the error to a dump file 
if [ $? -ne 0 ] ;then
	# If we could not access, return an error
	echo No directory with that name
	exit 1
fi
#If we got where we wanted, proceed
ls -Rl |  grep "\(^.\{4\}-\{3\}\)" | tr -s " " | cut -d' ' -f9 | while read file; do echo $file > text.txt; chmod g+r $file; done
cd .. ; rm dump.txt
# Clear the dump file
