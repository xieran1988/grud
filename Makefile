
all: proc.svg
	firefox $<

%.svg: %.dot
	dot -Tsvg $< > $@ || { rm $@; exit 1; }

dep: dep.pl
	./$< > $@

dep.dot: dep dot.pl
	./dot.pl < dep > $@

proc.dot: proc.pl dot.pl
	./proc.pl | ./dot.pl > $@

