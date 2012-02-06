#!/usr/bin/perl

open F, "ls /proc/*/exe | xargs -i@ readlink @ | sort | uniq |";
my $i = 0;
while (<F>) {
	chomp;
	my $e = $_;
	open L, "./ldd.sh $e |";
	while (<L>) {
		chomp;
		print "$e $_\n";
	}
	$i++;
	exit if $i == 3;
}
