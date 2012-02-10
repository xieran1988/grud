#!/bin/bash

while true ; do
	./pstree.pl | ./nc.pl 127.0.0.1 1900
	sleep 1
done

