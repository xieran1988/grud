#!/usr/bin/perl

my %h;
open F, "sudo ps -eo comm,pid,ppid,user | sed 1d |";
while (<F>) {
	chomp;
	my ($comm, $pid, $ppid, $user) = split /\s+/;
	$h{$pid} = $comm;
	print "pstree\t$comm\t$h{$ppid}\t$user\n" if exists $h{$ppid};
}

