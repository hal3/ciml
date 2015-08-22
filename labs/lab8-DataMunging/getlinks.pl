#!/usr/bin/perl -w
use strict;
while (<>) {
    while (s/<a[^>]*href="([^"]+)"//) { print "$1\n"; }
    while (s/<a[^>]*href=([^ >]+)//) { print "$1\n"; }
}
