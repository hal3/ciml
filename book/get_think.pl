#!/usr/bin/perl -w
use strict;

my $in = 0;
while (<>) {
  chomp;
  if (s/^\\thinkaboutit{//) {
      print '{' . $_; $in = 1;
  } elsif ($in && (/^[\s]*$/)) {
      $in = 0; print "\n";
  } elsif ($in) { 
      s/^\s*//; s/\s*$//;
      print ' ' . $_;
  }
}
if ($in) { print "\n"; }

