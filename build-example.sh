#!/bin/sh -e

if [ $# -ne 1 ] ; then
	echo "Usage: $0 <example>"
	exit 1
fi

example=$1
if [ ! -d $example ] ; then
	echo "$example does not exist"
fi

cd $example
docker -H ssh://fio@raspberrypi3-64-1 build -t $example --label aktualizr-no-prune .
