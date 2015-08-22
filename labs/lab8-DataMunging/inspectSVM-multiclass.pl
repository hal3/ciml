#!/usr/bin/perl -w
use strict;

my $USAGE = "usage: inspectSVM-multiclass.pl filename label label2?\nwhere: filename is the libsvm model file\n       label    is the label you want to know about\n       label2   is an optional label to compare 'label' to\nin other words, calling with one label gives you features that are indicative of that one label versus _all_ others; calling with two labels gives you information about A vs B where A is positive and B is negative\n";

my $filename = shift or die $USAGE;
my $label = shift or die $USAGE;
my $label2 = '';
while (1) { my $tmp = shift or last; $label2 = $tmp; last; }

my %dict = ();
open F, "libsvm.dict" or die;
while (<F>) {
    chomp;
    my ($n,$w) = split;
    $dict{$n} = $w;
}
close F;

my %w = ();
my %label2pos = ();
my %pos2label = ();
my $nr_class = 0;
open F, "$filename" or die;
while (<F>) {
    chomp;
    if (/^kernel_type (.+)$/) {
        my $kernel = $1;
        if ($kernel ne 'linear') { die "cannot expect nonlinear model"; }
    }
    if (/^label (.+)$/) {
        my @map = split /\s+/, $1;
        for (my $i=0; $i<@map; $i++) {
            $label2pos{$map[$i]} = $i;
            $pos2label{$i} = $map[$i];
        }
        if (not defined $label2pos{$label}) {
            die "you specified an invalid label '$label', the model only has labels '$1'";
        }
        if (($label2 ne '') && (not defined $label2pos{$label2})) {
            die "you specified an invalid label '$label2', the model only has labels '$1'";
        }
    }
    if (/^nr_class ([0-9]+)$/) { $nr_class = $1; }
    if (/^nr_sv (.+)$/) {
        my @nr_sv = split /\s+/, $1;
        $_ = <F>;
        chomp;
        if (not /^SV/) { die "malformed model file"; }

        for (my $pos=0; $pos<@nr_sv; $pos++) {
            my $l1 = $pos2label{$l1};
            for (my $svNum=0; $svNum<$nr_sv[$labelId]; $svNum++) {
                $_ = <F>;
                chomp;

                my @all = split;
                my $addAmount = 0;
                $addAmount += $all[$label2pos{$label}];
                if ($label2 ne '') {
                    $addAmount -= $all[$label2pos{$label2}];
                } else {
            for (my $i=0; $i<$nr_class; $i++) {
                if ($i == $label2pos{$label}) { next; }
                $addAmount -= $all[$i];
            }
        }
        for (my $i=$nr_class; $i<@all; $i++) {
            $all[$i] =~ /^([0-9]+):(.+)$/;
            $w{$dict{$1}} += $addAmount * $2;
        }
    }
}
close F;

foreach my $f (sort { $w{$b} <=> $w{$a} } keys %w) {
    print $w{$f} . "\t" . $f . "\n";
}
