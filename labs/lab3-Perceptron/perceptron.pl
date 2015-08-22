#!/usr/bin/perl -w
use strict;

my $MAXPASSES = 10;
my $DOAVERAGING = 0;

my $trFN = shift or die;
my @teFN = ($trFN);
while (1) {
    my $tmp = shift or last;
    push @teFN, $tmp;
}

my %w = ();  my $bias = 0;
my %u = ();  my $beta = 0;
my $c = 1;

my %predW = ();
my $predB = 0;

for (my $pass=1; $pass<=$MAXPASSES; $pass++) {
    print STDERR "$pass";
    open F, $trFN or die;
    while (<F>) {
        chomp;
        my ($y,@x) = split;
        $y = ($y < 0.5) ? -1 : +1;
        my $a = predict(\%w, $bias, @x);
        if ($a * $y <= 0) {
            increment(\%w, $y, @x);
            $bias += $y;
            increment(\%u, $y * $c, @x);
            $beta += $y * $c;
        }
        $c++;
    }
    close F or die;

    %predW = ();
    $predB = 0;
    if ($DOAVERAGING) {
        foreach my $x (keys %w) {
            $predW{$x} = $w{$x} - $u{$x} / $c;
        }
        $predB = $bias - (1/$c) * $beta;
    } else {
        %predW = %w;
        $predB = $bias;
    }

    foreach my $teFN (@teFN) {
        my $err = 0;
        my $N = 0;
        open F, $teFN or die;
        while (<F>) {
            chomp;
            my ($y,@x) = split;
            $y = ($y < 0.5) ? -1 : +1;
            my $a = predict(\%predW, $predB, @x);
            if ($a * $y <= 0) { $err++; }
            $N++;
        }
        close F or die;

        print STDERR "\t" . (int($err*1000/$N)/10);
    }
    print STDERR "\n";
}

print $predB . "\t**BIAS**\n";
foreach my $x (sort { $predW{$a} <=> $predW{$b} } keys %predW) {
    print $predW{$x} . "\t" . $x . "\n";
}


sub predict {
    my ($W, $B, @x) = @_;
    my $yhat = $B;
    foreach my $x (@x) {
        if (defined $W->{$x}) { $yhat += $W->{$x}; }
    }
    return $yhat;
}

sub increment {
    my ($W, $incr, @x) = @_;
    foreach my $x (@x) {
        $W->{$x} += $incr;
    }
}
