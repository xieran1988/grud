#!/bin/bash

tmp=`mktemp -d`
cd $tmp
cat > a.c <<E
#include <stdio.h>
int main() { sleep(20); return 0; }
E
gcc a.c
for i in `seq 1 50`; do
	cp a.out $i
	./$i &
done
wait
rm -rf $tmp
