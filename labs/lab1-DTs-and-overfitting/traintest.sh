#!/bin/bash

if [[ $# != 2 ]] ; then
  echo "usage: traintest.sh [dataset] [max depth]"
  exit -1
fi
if [[ ! -e "data/$1.tr" ]] ; then
  echo "training data 'data/$1.tr' not found"
  exit -1
fi
if [[ ! -e "data/$1.de" ]] ; then
  echo "development data 'data/$1.de' not found"
  exit -1
fi
if [[ ! -e "data/$1.te" ]] ; then
  echo "test data 'data/$1.te' not found"
  exit -1
fi

( FastDT -maxd $2 -minfc 0 data/$1.tr > output/$1.dt-$2 ) > /dev/null 2>&1
trErr=`( FastDT -load output/$1.dt-$2 data/$1.tr > output/$1.tr.pred-$4 ) 2>&1 | grep ^Error | cut -d' ' -f7`
deErr=`( FastDT -load output/$1.dt-$2 data/$1.de > output/$1.de.pred-$4 ) 2>&1 | grep ^Error | cut -d' ' -f7`
teErr=`( FastDT -load output/$1.dt-$2 data/$1.te > output/$1.te.pred-$4 ) 2>&1 | grep ^Error | cut -d' ' -f7`
echo "$2 $trErr $deErr $teErr"

