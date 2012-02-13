#!/usr/bin/python

import marshal, socket, sys
from igraph import *

if 0:
	G = Graph.Full(n=4, directed=True)
	for a in {'1':2, 2:3}:
		print a
	G.vs[1]['name'] = 'aa'
	G.vs[2]['name'] = 'bb'
	G.vs[1]['a'] = 1
	print G.vs[1]
	print G.pagerank()
	sys.exit(0)

def graph_init():
	global G 
	G = Graph(n=0, directed=True)
	G.vs['name'] = []

def proc2so_load():
	global proc2so
	proc2so = marshal.load(open('proc2so.cache'))

def add_node(name, **kw):
	if name not in G.vs['name']:
		G.add_vertices(1)
		kw['name'] = name
		for k in kw:
			G.vs[G.vcount() - 1][k] = kw[k];
		G[name] = G.vcount() - 1

def add_inode(inode):
	add_node(inode, cat='inode')

def add_so(so):
	add_node(so, cat='so')

def add_proc(proc):
	add_node(proc, cat='proc')
	if proc in proc2so:
		for so in proc2so[proc]:
			add_so(so)
			add_edge(proc, so)

def add_edge(a, b):
	if a != b:
		G.add_edges((G[a], G[b]))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind(('', 1900))
so2so = marshal.load(open('so2so.cache'))
proc2so_load()
graph_init()

while 1:
	msg, addr = s.recvfrom(65536)
#	print 'msg=,',msg
	a = msg.strip().split('\t')
	func = a[0]
	if func == 'ext4_file_mmap' or func == 'ext4_readdir': 
		proc, inode = a[1:]
		add_proc(proc)
		add_inode(inode)
		add_edge(proc, inode)
	elif func == 'tcp_v4_rcv' or func == 'tcp_recvmsg':
		proc, saddr, sport, daddr, dport = a[1:]
		add_proc(proc)
	elif func == 'pstree':
		proc, child = a[1:]
		add_proc(proc)
		add_proc(child)
		add_edge(child, proc)
	elif func == 'proc2so':
#		print func
		proc2so_load()
	elif func == 'gengraph':
		print func
		print '---- graph ----'
		summary(G)
		print '---- pagerank ----'
		pr = G.pagerank()
#		print [ v for v in G.vs.select(cat='so')][:25]
		for i in map(lambda x: x[1], \
				sorted([ (pr[i], G.vs[i]['name']) for i in range(len(pr)) ], reverse=True)[:25]) \
				:
			print i, pr[G[i]]
		print '---------'
		graph_init()

'''
f = open('algo.graph', 'w+')
for i in E:
	for j in E[i]:
		f.write('%s\t%s\n'%(i,j))
f.close()
'''

