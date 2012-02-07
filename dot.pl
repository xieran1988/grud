#!/usr/bin/perl

print <<EOF;
digraph dis {
	graph [size="400,400"];
EOF
while (<>) {
	chomp;
	my @a = split /\t/; 
	print "\"$a[0]\" -> \"$a[1]\";\n";
}
print "}\n";
