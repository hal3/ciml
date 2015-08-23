#!/usr/bin/perl -w
use strict;

my $fn1 = shift or die;
my $fn2 = shift or die;

my %a = readFile($fn1);
my %b = readFile($fn2);

my %c = ();
foreach my $x (keys %a) {
    if (defined $b{$x}) {
        $c{$x} = $a{$x} * $b{$x};
    }
}

foreach my $x (sort { $c{$b} <=> $c{$a} } keys %c) {
    print '' . $c{$x} . "\t" . $x . "\n";
}

sub readFile {
    my ($fn) = @_;
    my %h = ();
    open F, $fn or die;
    while (<F>) {
        chomp;
        my ($w,$x) = split;
        $h{$x} = $w;
    }
    close F or die;
    return (%h);
}
