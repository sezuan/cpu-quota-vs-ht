#!/bin/bash
for threads in `seq 1 8`;do docker run --cpu-quota 200000 --cpu-period 100000 --rm -ti cpu-limit $threads 2000 | grep rate:;done
