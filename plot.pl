#!/usr/bin/perl

`rm -rf *.pti`;
open F, "cat algo.cols |";
my %png;
while (<F>) {
	chomp;
	next if $. == 1;
	print "$_: $.\n";
	my ($c, $f) = split /:/;
	$png{$c}++;
	if ( ! -e "$c.pti") {
`echo '
set terminal png 
set output "$c.png"
set xlabel "time"
set ylabel "value"
set urange [0:10]
set title "$c"
set autoscale
plot \\' > $c.pti`;
	}
	`echo '\"algo.out\" using 1:$. w lp pt 5 title \"$f\",\\' >> $c.pti`;
}
close F;
system("sed -i '\$s/,\\\\//' *.pti");
#`sed -i '\$d' *.pti`;

open I, ">algo.html";
print I "<body>\n";
print I "<meta http-equiv=refresh content=1 />\n";
for my $k (keys %png) {
	print I "<img src=/grud/$k.png width=320/>";
}
print I "</body>\n";
close I;

for my $k (keys %png) {
	`gnuplot $k.pti`;
}

