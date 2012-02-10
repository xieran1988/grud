#!/usr/bin/perl

use Socket;

socket(S, PF_INET, SOCK_DGRAM, getprotobyname("udp"));
my $addr = sockaddr_in($ARGV[1], inet_aton($ARGV[0]));

while (<STDIN>) {
	send(S, $_, 0, $addr);
}



