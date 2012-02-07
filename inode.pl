#!/usr/bin/perl

my %so2so;
my %proc2so;
my %E;
my %V;

open F, "/tmp/inode.log";
while (<F>) {
	my ($proc, $pid, $func, $ino, $rw) = split /,/;
	$E{$proc}{$ino} = "frw";
}

while (<F>) {

}

open F, ""

