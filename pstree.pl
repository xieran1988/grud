#!/usr/bin/perl

my %h;
open F, "sudo ps -eo comm,pid,ppid | sed 1d |";
while (<F>) {
	chomp;
	my ($comm, $pid, $ppid) = split /\s+/;
	$h{$pid} = $comm;
	print "pstree\t$comm\t$h{$ppid}\n" if exists $h{$ppid};
}

