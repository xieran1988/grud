#!/usr/bin/perl

while (<>) {
	my $so = `basename $_`;
	chomp $so;
	open L, "./ldd.sh $_ |";
	while (<L>) {
		chomp;
		print "$so\t$_\n";
	}
}

