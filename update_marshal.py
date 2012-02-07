#!/usr/bin/python

import marshal, sys, os

cachefile = sys.argv[1]
listfile = sys.argv[2]
m = marshal.load(open(cachefile)) if os.path.exists(cachefile) else {}
for l in open(listfile).readlines():
	a, b = l.split('\t')
	if a not in m:
		m[a] = {}
	m[a][b] = 1
marshal.dump(m, open(cachefile, 'wb+'))

