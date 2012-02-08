#!/usr/bin/perl

open F, "ps -eo comm,pid | sed 1d |";
while (<F>) {
	chomp;
	my ($comm, $pid) = split /\s+/;
	my $f = "proc2so/$comm.list";
	`ldd /proc/$pid/exe | awk -v c=$comm '{print c"\t"\$1}' > $f` if (not -e $f);
}

