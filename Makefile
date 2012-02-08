
all: algo.graph

results := inoderw.result netuse.result pstree.result 

force:

%.png: %.dot
	dot -Tpng $< > $@ || { rm $@; exit 1; }

algo.graph: algo.py proc2so.cache so2so.cache ${results}
	./algo.py

algo-graph.dot: dot.pl algo.graph
	./dot.pl < algo.graph > $@

%.cache: %.pl update_marshal.py force
	mkdir -p $*
	./$<
	cat $*/* | ./update_marshal.py $@

netuse.result:
	sudo lsof -i4 | sed '1d' | awk '{print $$1,$$8,$$9}' | ./netuse.pl > $@

inoderw.result:
	sudo stap inode.stp > $@

pstree.result:
	echo "bash	ls" > $@
	echo "ls	ls" >> $@

clean:
	rm -rf *.result proc2so.list

setup:
#	http://ddebs.ubuntu.com/pool/main/l/linux/linux-image-3.0.0-12-generic-dbgsym_3.0.0-12.20_i386.ddeb

