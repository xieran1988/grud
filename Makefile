
all: algo-graph.svg
	firefox $<

%.svg: %.dot
	dot -Tsvg $< > $@ || { rm $@; exit 1; }

algo-graph.dot: dot.pl algo.graph
	./dot.pl < algo.graph > $@

%.cache: %.list update_marshal.py
	./update_marshal.py $@ $<

netuse.result:

proc2so.list: inoderw.result netuse.result pstree.result
	cat $^ | awk '{print $$1}' | ./ldd.pl > $@

so2so.list:
	sudo find /usr/lib/ -name '*so*' | grep 'so\.[^\.]*$$'| ./ldd.pl > $@

so.so.dot: so.so.cache dot.pl
	./dot.pl < $< > $@

proc.dot: proc.pl dot.pl
	./proc.pl | ./dot.pl > $@

setup:
#	http://ddebs.ubuntu.com/pool/main/l/linux/linux-image-3.0.0-12-generic-dbgsym_3.0.0-12.20_i386.ddeb



