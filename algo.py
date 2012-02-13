#!/usr/bin/python

import marshal, socket, sys
from igraph import *

def graph_init():
	G = Graph(n=0, directed=True)
	V = {}
	return G, V

def proc2so_load():
	return marshal.load(open('proc2so.cache'))

def add_inode(inode):
	if inode not in V:
		V[inode] = {'type': 'inode', 'val': inode, 'no': G.vcount()} 
		G.add_vertices(1)
	return V[inode]['no']

def add_so(so):
	if so not in V:
		V[so] = {'type': 'so', 'val': so, 'no': G.vcount()}
		G.add_vertices(1)
	return V[so]['no']

def add_proc(proc):
	if proc not in V:
		V[proc] = {'type': 'proc', 'val': proc, 'no': G.vcount()}
		G.add_vertices(1)
		if proc in proc2so:
			G.add_edges([(V[proc]['no'], add_so(so)) for so in proc2so[proc]])
	return V[proc]['no']

def add_edge(a, b):
	na = V[a]['no']
	nb = V[b]['no']
	if na != nb:
		G.add_edges((na, nb))

def subject_rank():
	return 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind(('', 1900))
so2so = marshal.load(open('so2so.cache'))
proc2so = proc2so_load()
G, V = graph_init()

while 1:
	msg, addr = s.recvfrom(65536)
#	print 'msg=,',msg
	a = msg.strip().split('\t')
	func = a[0]
	if func == 'ext4_file_mmap' or func == 'ext4_readdir': 
		proc, inode = a[1:]
		add_proc(proc)
		add_inode(inode)
		add_edge(inode, proc)
	elif func == 'tcp_v4_rcv' or func == 'tcp_recvmsg':
		proc, saddr, sport, daddr, dport = a[1:]
		add_proc(proc)
	elif func == 'pstree':
		proc, child = a[1:]
		add_proc(proc)
		add_proc(child)
		add_edge(proc, child)
	elif func == 'proc2so':
		print func
		proc2so = proc2so_load()
	elif func == 'gengraph':
		print func
		print '-----------'
		summary(G)
		G, V = graph_init()

'''
f = open('algo.graph', 'w+')
for i in E:
	for j in E[i]:
		f.write('%s\t%s\n'%(i,j))
f.close()
'''

