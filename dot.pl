#!/usr/bin/perl

print <<EOF;
digraph dis {
	ratio=auto;
	size="7,7";
	ranksep="1.0 equally";
EOF
while (<>) {
	chomp;
	my @a = split /\t/; 
	print "\"$a[0]\" -> \"$a[1]\";\n";
}
print "}\n";
