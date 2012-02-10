#!/usr/bin/perl

open F, "ps -eo comm,pid | sed 1d |";
while (<F>) {
	chomp;
	my ($comm, $pid) = split /\s+/;
	next if $comm =~ /\//;
	my $f = "proc2so/$comm.list";
	if (not -e $f) {
		`ldd /proc/$pid/exe | awk -v c=$comm '{print c"\t"\$1}' > $f`;
	}
}

