#!/bin/bash

./$1.pl
mkdir -p $1
cat $1/* | ./update_marshal.py $1.cache

