#!/bin/bash

clear
cd "/media/Rpi3B+Download/Download"
echo "============================================================================================================="
echo " ------------------------- it will work on '/media/Rpi3B+Download/Download' directory ----------------------- "
echo "shell to move the downloaded file which are one per directory"
echo "to a unique directory. the new directory name has to be contained"
echo "in the downloaded directory name."
echo " es : "
echo "    downloaded dir name : Star.Trek.Strange.New.Worlds.S01E05.Buffo.Come.Spock.WEBMux.720P.ITA.ENG.AC3.x264-Prometheus"
echo "    new directory name  : Strange "
echo "the shell will find for all the dir name which contain 'Strange' and move the files contained to the 'Strange' dir"
echo "============================================================================================================="
# NAME=Strange

echo " type the name of the new directory name (beware it is case sensitive) :"
read NAME

mkdir -v $NAME

find . -maxdepth 1 -mindepth 1 -type d | grep $NAME | while read dir; 
  do
    cd "$dir"
    find . -type f | while read myfile ; 
    do
      echo "trovato file $myfile -----------------"
      mv $myfile  "/media/Rpi3B+Download/Download/$NAME"
      echo "moved $myfile to $NAME"
    done 
    # echo "$dir"
    ls -l 
    cd .. 
  done 
echo "=================================================================="

echo "Fine utility "
read pippo
