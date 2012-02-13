#!/bin/bash

while true; do
	./update_cache.sh proc2so 2> /dev/null
	echo proc2so | ./nc.pl 127.0.0.1 1900
	sleep 1
done

