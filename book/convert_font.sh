#!/bin/bash

fontname=$1

if [[ -e $fontname.ttf ]] ; then
  ttf2afm -e T1-WGL4.enc -o $fontname.afm $fontname.ttf
  afm2tfm $fontname.afm -T T1-WGL4.enc
  echo "$fontname $fontname.ttf Encoding=T1-WGL4.enc" >> ttfonts.map

  echo "\\ProvidesFile{t1$fontname.fd}[$fontname Font]" > t1$fontname.fd
  echo "\\DeclareFontFamily{T1}{$fontname}{}" >> t1$fontname.fd
  echo "\\DeclareFontShape{T1}{$fontname}{m}{n}{ <-> $fontname}{}" >> t1$fontname.fd
else
  echo "$fontname.ttf not found!"
fi
