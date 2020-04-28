#!/bin/bash

echo $1 | sed 's/\(.\)/\1\'$'\n/g' | grep [aeiouAEIOU] | wc -l | tr -s ' '
