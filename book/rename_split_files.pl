#!/usr/bin/perl -w
use strict;

my %chapters = ();
my $firstChapter = 99999;
my $maxChapter = 0;
open F, "courseml.toc" or die;
while (<F>) {
    chomp;
    if (/{chapter}{\\numberline {([0-9]+)}[^}]+}{([0-9]+)}/) {
        $chapters{$2} = $1;
        if ($2 < $firstChapter) { $firstChapter = $2; }
        if ($1 > $maxChapter) { $maxChapter = $1; }
    }
    elsif (/{chapter}{[^}]+}{([0-9]+)}/) {
        $chapters{$1} = 0;
    }
}
close F;

my @cover = ('cover/cover.pdf');
{
    `pdfsam-console -f foo/1_courseml.pdf -o foo/coverinfo/ -s BURST split`;
    if ((-e 'foo/coverinfo/1_1_courseml.pdf') && (-e 'foo/coverinfo/2_1_courseml.pdf')) {
        @cover = ('foo/coverinfo/1_1_courseml.pdf', 'foo/coverinfo/2_1_courseml.pdf');
    }
}

my $VER = `cat version`; chomp $VER;
$VER =~ s/\./_/g;

if (-e "ciml-v$VER") { die "directory ciml-v$VER already exists.\nplease delete first or edit version.\n"; }

`mkdir ciml-v$VER`;
`cp courseml.pdf ciml-v$VER/ciml-v$VER-all.pdf`;

my @front = (); my @back = @cover;

open LS, "ls foo/*.pdf|" or die;
while (my $fname = <LS>) {
    chomp $fname;
    if ($fname =~ /\/([0-9]+)_courseml\.pdf$/) {
        my $N = $1;
        if ((not defined $chapters{$N}) || ($chapters{$N} == 0)) {
            if ($N < $firstChapter) {
                push @front, ('foo/' . $N . '_courseml.pdf');
            } else {
                push @back,  ('foo/' . $N . '_courseml.pdf');
            }
        } else {
            my $ch = $chapters{$N};
            if ($ch < 10) { $ch = '0' . $ch; }
            if ($ch > 0) {
                merge($ch, @cover, $fname);
            }
        }
    }
}
close LS;

merge('00'         , sort { $a <=> $b } @front);
merge($maxChapter+1, sort { $a <=> $b } @back );

sub merge {
    my ($outN, @in) = @_;
    my $cmd = "pdfsam-console -o ciml-v$VER/ciml-v$VER-ch$outN.pdf";
    foreach my $x (@in) { $cmd .= ' -f ' . $x; }
    $cmd .= ' concat';
    print $cmd . "\n";
    system($cmd);
}

