#!/usr/bin/python

import marshal, sys, os

cachefile = sys.argv[1]

if os.path.exists(cachefile):
	f = open(cachefile, 'rb')
	m = marshal.load(f)
	f.close()
else:
	m = {}

for l in sys.stdin.readlines():
	a, b = l.strip().split('\t')
	if a not in m:
		m[a] = {}
	m[a][b] = 1

f = open(cachefile, 'wb+') 
marshal.dump(m, f)
f.close()

