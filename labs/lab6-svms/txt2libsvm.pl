#!/usr/bin/perl -w
use strict;

my $y = 0;
my @d = ();
my $maxX = 0;
while (<>) {
    chomp;
    for (my $x=0; $x<length($_); $x++) {
        if (substr($_,$x,1) eq '+') {
            push @d, "+1 $x $y";
        } elsif (substr($_,$x,1) eq '-') {
            push @d, "-1 $x $y";
        }
    }
    if (length($_) > $maxX) { $maxX = length($_); }
    $y++;
}
my $maxY = $y-1;
$maxX--;

for (my $n=0; $n<@d; $n++) {
    my ($y,$x1,$x2) = split /\s+/, $d[$n];
    $x1 /= $maxX;
    $x1 -= 0.5;
    $x2 /= $maxY;
    $x2 -= 0.5;
    print "$y 1:$x1 2:$x2\n";
}

