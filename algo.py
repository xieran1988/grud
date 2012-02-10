#!/usr/bin/python

import marshal, socket

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
		if proc in proc2so:
			for so in proc2so[proc]:
				add_so(so)
				if proc not in E:
					E[proc] = {}
				E[proc][so] = 1

def add_edge(a, b):
	if a not in E:
		E[a] = {}
	E[a][b] = 1

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind(('', 1900))
while 1:
	msg, addr = s.recvfrom(65536)
	print 'msg=,',msg
	a = msg.strip().split('\t')
	func = a[0]
	if func == 'ext4_file_mmap': 
		proc, inode = a[1:]
		add_proc(proc)
		add_inode(inode)
		add_edge(inode, proc)
	elif func == 'tcp_v4_rcv':
		proc, saddr, sport, daddr, dport = a[1:]
		add_proc(proc)
	elif func == 'pstree':
		proc, child = a[1:]
		add_proc(proc)
		add_proc(child)
		add_edge(proc, child)
	elif func == 'proc2so':
		proc2so = marshal.load(open('proc2so.cache'))

f = open('algo.graph', 'w+')
for i in E:
	for j in E[i]:
		f.write('%s\t%s\n'%(i,j))
f.close()

