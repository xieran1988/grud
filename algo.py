#!/usr/bin/python

import marshal

V = {}
E = {}
proc2so = marshal.load(open('proc2so.cache'))
so2so = marshal.load(open('so2so.cache'))

def add_inode(inode):
	if inode not in V:
		V[inode] = 'i'

def add_so(so):
	if so not in V:
		V[so] = 's'

def add_proc(proc):
	if proc not in V:
		V[proc] = 'p'
		for so in proc2so[proc]:
			add_so(so)
			if proc not in E:
				E[proc] = {}
			E[proc][so] = 1

def add_edge(a, b):
	if a not in E:
		E[a] = {}
	E[a][b] = 1

for l in open('inoderw.result').readlines():
	proc, inode = l.strip().split('\t')
	add_proc(proc)
	add_inode(inode)
	add_edge(inode, proc)

for l in open('netuse.result').readlines():
	proc, port = l.strip().split('\t')
	add_proc(proc)

for l in open('pstree.result').readlines():
	proc, child = l.strip().split('\t')
	add_proc(proc)
	add_proc(child)
	add_edge(proc, child)
	
f = open('algo.graph', 'w+')
for i in E:
	for j in E[i]:
		f.write('%s\t%s\n'%(i,j))
f.close()

