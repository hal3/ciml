#!/usr/bin/perl -w
use strict;

my @chap = ();

$chap[0] = 1;
open F, "courseml.toc" or die;
while (<F>) {
    chomp;
    if (/\\contentsline {chapter}{\\numberline {([0-9]+)}[^}]+}{([0-9]+)}{/) {
        my $ch = $1;
        my $pg = $2;
        $chap[$ch] = $pg;
    }
}
close F or die;

for (my $i=0; $i<@chap; $i++) {
    print "$i\t$chap[$i]\n";
}
