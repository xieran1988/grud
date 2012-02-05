#!/usr/bin/perl

open F, "find /lib /usr/lib -name '*so*' |";
my $i = 0;
while (<F>) {
	next unless /so\.[^.]+$/;
	my $so = `basename $_`;
	chomp $so;
	$i++;
	exit if ($i == 3);
	open L, "./ldd.sh $_ |";
	while (<L>) {
		chomp;
		print "$so $_\n";
	}
}
