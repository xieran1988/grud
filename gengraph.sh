#!/bin/bash

while true; do
	echo gengraph | ./nc.pl 127.0.0.1 1900
	sleep 3
done

