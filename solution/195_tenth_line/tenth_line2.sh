#!/usr/bin/env bash

set -e

awk 'NR == 10 {print $0}' file.txt
