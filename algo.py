#!/usr/bin/python

import marshal, socket, sys, time, os
from igraph import *

def graph_init():
	global G, E
	G = Graph(n=0, directed=True)
	G.vs['name'] = []
	E = {}

def proc2so_load():
	global proc2so
	proc2so = marshal.load(open('proc2so.cache'))

def add_node(name, **kw):
	if name not in G.vs['name']:
		dstat('nodes:'+kw['cat'])
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
	if a != b and (a,b) not in E:
		E[(a,b)] = 1

def dstat(f, n=1):
	global colstbl
	if f not in cols:
		cols[f] = 0
	if f not in colstbl:
		colstbl += [f]
	cols[f] += n

rows = []
cols = {}
colstbl = []
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 1900))
so2so = marshal.load(open('so2so.cache'))
proc2so_load()
graph_init()
gn = 0

while 1:
	msg, addr = s.recvfrom(1024)
	a = msg.strip().split('\t')
	func = a[0]
	if func == 'ext4_file_mmap' or func == 'ext4_readdir': 
		dstat('funcs:'+func)
		proc, inode = a[1:]
		add_proc(proc)
		add_inode(inode)
		add_edge(proc, inode)
	elif func == 'tcp_v4_rcv' or func == 'tcp_recvmsg':
		proc, saddr, sport, daddr, dport = a[1:]
		dstat('funcs:'+func);
		add_proc(proc)
	elif func == 'pstree':
		proc, child = a[1:]
		dstat('funcs:'+func)
		add_proc(proc)
		add_proc(child)
		add_edge(child, proc)
	elif func == 'proc2so':
		proc2so_load()
		pass
	elif func == 'gengraph':
		gn += 1

		for a,b in E:
			G.add_edges((G[a], G[b]))

		print '##### graph %d ----' % gn
		summary(G)
		print '---- pagerank ----'
		pr = G.pagerank()
#		print [ v for v in G.vs.select(cat='so')][:25]
		for i in map(lambda x: x[1], \
				sorted([ (pr[i], G.vs[i]['name']) for i in range(len(pr)) ], reverse=True)[:5]) \
				:
			print i, pr[G[i]]
		print

		dstat('edges:edges_nr', G.ecount())
		#dstat('nodes:nodes_nr', G.vcount())

		rows.append(cols)

		for c in colstbl:
			f = open('algo.cols', 'w+')
			f.write('\n'.join(['x'] + colstbl)+'\n')
			f.close()

		f = open('algo.out', 'w+')
		for i in range(len(rows)):
			c = rows[i]
			f.write(' '.join([str(i)] + [ str(c[k] if k in c else 0) for k in colstbl]) + '\n')
		f.close()

#		if gn == 10:
#			sys.exit(0)

		cols = {}

		os.system('./plot.pl')

		graph_init()

'''
f = open('algo.graph', 'w+')
for i in E:
	for j in E[i]:
		f.write('%s\t%s\n'%(i,j))
f.close()
'''

