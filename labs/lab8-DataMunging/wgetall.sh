#!/bin/bash

if [[ "$#" -ne "2" ]] ; then
  echo usage: getall.sh [input file] [output directory]
  exit -1
fi

filename=$1
dir=$2

if [[ ! -e $dir ]] ; then
  mkdir $dir
fi

n=1
for url in `cat $filename` ; do
  wget -O $dir/$n.html "$url"
  let n=$n+1
done
