#!/bin/bash
for n in {42..43}
do
    for h in {1..100}
    do
                ping -c 1 190.168.$n.$h | grep "bytes from" |cut -d " " -f4 | cut -d ":" -f1 &
    done
done
