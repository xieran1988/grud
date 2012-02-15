#!/bin/bash

i=0
while true; do
	((i++))
	echo "graph $i"
	./update_cache.sh proc2so 2> /dev/null
	echo proc2so | ./nc.pl 127.0.0.1 1900
	./pstree.pl | ./nc.pl 127.0.0.1 1900
	echo gengraph | ./nc.pl 127.0.0.1 1900
	sleep 2
done

