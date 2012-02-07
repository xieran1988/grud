

all: algo-graph.png

results := inoderw.result netuse.result pstree.result 

force:

%.png: %.dot
	dot -Tpng $< > $@ || { rm $@; exit 1; }

algo.graph: algo.py proc2so.cache so2so.cache ${results}
	./algo.py

algo-graph.dot: dot.pl algo.graph
	./dot.pl < algo.graph > $@

%.cache: %.list update_marshal.py
	./update_marshal.py $@ $<

netuse.result:
	echo "sshd	22" > $@

inoderw.result:
	echo "awk	332cc" > $@

pstree.result:
	echo "bash	ls" > $@
	echo "ls	ls" >> $@

proc2so.list: ${results} ldd.pl
	cat ${results} | awk '{print $$1}' | sort | uniq | xargs -i@ which @ | ./ldd.pl > $@

so2so.list: ldd.pl
	sudo find /usr/lib/ -name '*so*' | grep 'so\.[^\.]*$$'| ./ldd.pl > $@

clean:
	rm -rf *.result proc2so.list

setup:
#	http://ddebs.ubuntu.com/pool/main/l/linux/linux-image-3.0.0-12-generic-dbgsym_3.0.0-12.20_i386.ddeb

