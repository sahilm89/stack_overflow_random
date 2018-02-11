#!/usr/bin/perl
use strict;
use warnings;

my $filename = '5000_lines.txt';
open ( DATA, '>', $filename )  or die "Could not open file '$filename': $!";

for (my $i=0;$i<5000;$i++){
    print DATA "$i\n";
}
close ( DATA);


my $targetfile = '200_lines.txt';

open ( my $DATA, '<', $filename )  or die "Could not open file '$filename': $!";
my $counter = 0;
my $num = 0;
my $flag = 1;
while ( my $line = <$DATA> ) {
      if ($flag == 1){
          open (FILE, '>', $targetfile.'_'.$num ) or die "Could not open file '$targetfile.'_'.$num': $!";
      }
      print FILE $line;
      $flag=0;
      if ( $counter % 200 == 0){
           $num = $counter/200;
           close FILE;
           $flag=1
       }
      $counter++; 
}
close FILE;
