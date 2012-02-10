
all: algo.graph

force:

%.png: %.dot
	dot -Tpng $< > $@ || { rm $@; exit 1; }

algo.graph: algo.py proc2so.cache so2so.cache 
	./algo.py

algo-graph.dot: dot.pl algo.graph
	./dot.pl < algo.graph > $@


