
all: dep.svg
	firefox $<

dep: dep.pl
	./$< > $@

dep.dot: dep dot.pl
	./dot.pl < dep > $@

dep.svg: dep.dot
	dot -Tsvg $< > $@ || { rm $@; exit 1; }


