#!/bin/bash

tmp=`mktemp -d`
cd $tmp
for i in `seq 1 30`; do
	for j in `seq 1 1000`; do
	done
	sleep 1
	rm -rf *
done
rm -rf $tmp
