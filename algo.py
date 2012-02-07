#!/usr/bin/python

import marshal

V = {}
E = {}
proc2so = marshal.load('proc2so.cache')
so2so = marshal.load('so2so.cache')

def add_inode(inode):
	if not V[inode]:
		V[inode] = 'i'

def add_so(so):
	if not V[so]:
		V[so] = 's'

def add_proc(proc):
	if not V[proc]:
		V[proc] = 'p'
		for so in proc2so[proc]:
			add_so(so)
			E[proc][so] = 1

for l in open('inoderw.result').readlines():
	proc, inode = l.split('\t')
	E[inode][proc] = 1
	add_proc(proc)
	add_inode(inode)

for l in open('netuse.result').readlines():
	proc, port = l.split('\t')
	add_proc(proc)

for l in open('pstree.result').readlines():
	proc, child = l.split('\t')
	E[proc][child] = 1
	add_proc(proc)
	add_proc(child)
	
f = open('algo.graph', 'w+')
for i in E:
	for j in E[i]:
		f.writeline('%s\t%s'%(i,j))

