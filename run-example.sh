#!/bin/sh -e

if [ $# -ne 1 ] ; then
	echo "Usage: $0 <example>"
	exit 1
fi

example=$1
cd $example
script=$(ls *.py)
docker -H ssh://fio@raspberrypi3-64-1 run --rm --privileged -it $example
