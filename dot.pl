#!/usr/bin/perl

print "digraph dis {\n";
while (<>) {
	chomp;
	my @a = split / /; 
	print "\"$a[0]\" -> \"$a[1]\";\n";
}
print "}\n";
