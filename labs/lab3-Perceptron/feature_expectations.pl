#!/usr/bin/perl -w
use strict;

my %e = ();
my $N = 0;
while (<>) {
    chomp;
    my ($y,@x) = split;
    foreach my $x (@x) { $e{$x}++; }
    $N++;
}

foreach my $x (sort { $e{$b} <=> $e{$a} } keys %e) {
    print '' . ($e{$x}/$N) . "\t" . $x . "\n";
}
