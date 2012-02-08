#!/usr/bin/perl

use File::Basename;

open F, "sudo find /usr/lib/ -name '*.so.*' -printf '%p\t%f\n' | grep 'so\.[^\.]*\$'| ";
while (<F>) {
	chomp;
	my ($so, $name) = split /\t/;
	my $f = "so2so/$name.list";
	`ldd $so | awk -v c=$name '{print c"\t"\$1}' > $f` if (not -e $f);
}

