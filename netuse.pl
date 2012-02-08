#!/usr/bin/perl

while (<>) {
	chomp;
	my ($proc, $prot, $net) = split / /;
#	print "$net\n";
	my ($src, $dst) = split /->/, $net;
	my ($dstip, $dstport) = split /:/, $dst;
	print "$proc\t$dstport\n" if $dstport;
}

