#!/usr/bin/perl -w
use strict;

my $filename = shift or die;

my %dict = ();
open F, "libsvm.dict" or die;
while (<F>) {
    chomp;
    my ($n,$w) = split;
    $dict{$n} = $w;
}
close F;

my %w = ();
my $inSV = 0;
open F, "$filename" or die;
while (<F>) {
    chomp;
    if (/^kernel_type (.+)$/) {
        my $kernel = $1;
        if ($kernel ne 'linear') { die "cannot expect nonlinear model"; }
    }
    if (/^SV/) { $inSV = 1; next; }
    if ($inSV) {
        my ($y, @fc) = split;
        foreach my $fc (@fc) {
            $fc =~ /^([0-9]+):(.+)$/;
            $w{$dict{$1}} += $y * $2;
        }
    }
}
close F;

foreach my $f (sort { $w{$b} <=> $w{$a} } keys %w) {
    print $w{$f} . "\t" . $f . "\n";
}
