#!/bin/bash
for threads in `seq 1 8`;do docker run --rm -ti cpu-limit $threads 2000 | grep rate:;done
