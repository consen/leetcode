#!/usr/bin/env bash

set -e

num=$(wc -l file.txt | cut -d ' ' -f 1)
if [ $num -ge 10 ]; then
    echo $(head -n 10 file.txt | tail -n 1)
fi
