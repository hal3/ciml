#!/usr/bin/perl -w
use strict;

my %dict = (); my $dictN = 1;
open O, ">libsvm.dict" or die;
while (<>) {
    chomp;
    my ($y,@x) = split;
    print $y;
    my %x = ();
    foreach my $x (@x) {
        if (not defined $dict{$x}) {
            print O "$dictN\t$x\n";
            $dict{$x} = $dictN;
            $dictN++;
        }
        $x{$dict{$x}}++;
    }
    foreach my $f (sort { $a <=> $b } keys %x) {
        print ' ' . $f . ':' . $x{$f};
    }
    print "\n";
}
close O;
