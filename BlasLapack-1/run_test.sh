#!/bin/bash

set -eux

g++ -std=c++17 -Wall -pedantic main.cpp -I ./cblas -o main
./main
