#!/usr/bin/perl -w
use strict;

print "<ol>\n";
open CML, "courseml.tex" or die;
while (<CML>) {
    chomp;
    if (/^\\include{(.+)}/) {
        my $fname = $1 . '.tex';
        includeFile($fname);
    }
}
close CML;
print "</ol>\n";

sub includeFile {
    my ($fname) = @_;

    my $cname = '';
    my @sec = ();
    my $inobj = 0;
    my $objStr = '';
    my $numW = 0;
    open F, $fname or die;
    while (<F>) {
        if (/\\chapter{([^}]+)}/) {
            $cname = $1;
        }
        elsif (/\\section{([^}]+)}/) {
            push @sec, $1;
        }
        elsif (/\\section\[([^\]]+)\]{/) {
            push @sec, $1;
        }
        if (/\\begin{learningobjectives}/) { $inobj = 1; }
        elsif (/\\end{learningobjectives}/) { $inobj = 0; }
        elsif ($inobj) { $objStr .= $_ . " "; }
        else {
            my @w = split;
            $numW += scalar @w;
        }
    }
    $objStr =~ s/^\s*\\item //g;
    my @obj = split /\\item /, $objStr;

    if ($cname eq '') { return; }

    print "<li>\n";
    print "  $cname <font size=-1>($numW words)</font>\n";
    if (@obj > 1) {
        print "  <span class=\"objectives\">\n";
        print "    <font size=\"-2\">[objectives]</font>\n";
        print "    <span>\n";
        print "      <ol>\n";
        foreach my $o (@obj) {
            $o =~ s/\s+/ /g; $o =~ s/\$//g; $o =~ s/^ //; $o =~ s/ $//;
            print "        <li> $o </li>\n";
        }
        print "      </ol>\n";
        print "    </span>\n";
        print "  </span>\n";
    }
    if (@sec > 0) {
        print "  <ul>\n";
        foreach my $s (@sec) {
            print "    <li>$s</li>\n";
        }
        print "  </ul>\n";
    }
    print "</li>\n";
}

