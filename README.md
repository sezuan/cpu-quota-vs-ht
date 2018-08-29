# cpu-quota-vs-ht

Demonstrates unexpected performance decrease when using CPU quota and hyper threading.

The script performs CPU bound operations with a configured number of threads.

Tested on a core i7 with 4 cores and 8 hyper threads.

## ht enabled, no CPU limit

    $ ./test_no_limit.sh 
    *** procs:  1 rate:  22.7 ***
    *** procs:  2 rate:  44.7 ***
    *** procs:  3 rate:  65.7 ***
    *** procs:  4 rate:  87.4 ***
    *** procs:  5 rate:  85.9 ***
    *** procs:  6 rate:  85.2 ***
    *** procs:  7 rate:  84.5 ***
    *** procs:  8 rate:  79.4 ***

Expected behavior, there's no benefit to run more threads than real cores.

## ht enabled, 2 CPU limit

    $ ./test_2cpu_limit.sh 
    *** procs:  1 rate:  22.2 ***
    *** procs:  2 rate:  44.0 ***
    *** procs:  3 rate:  41.2 ***
    *** procs:  4 rate:  42.0 ***
    *** procs:  5 rate:  29.9 ***
    *** procs:  6 rate:  27.5 ***
    *** procs:  7 rate:  23.7 ***
    *** procs:  8 rate:  22.0 ***

Unexpected behavior, performance decrease when there more threads than real cores.

## ht disabled, 2 CPU limit

    $ ./test_2cpu_limit.sh 
    *** procs:  1 rate:  22.5 ***
    *** procs:  2 rate:  43.0 ***
    *** procs:  3 rate:  43.2 ***
    *** procs:  4 rate:  43.2 ***
    *** procs:  5 rate:  44.5 ***
    *** procs:  6 rate:  44.5 ***
    *** procs:  7 rate:  44.7 ***
    *** procs:  8 rate:  45.2 ***

Expected behavior, performance unchanged when running more threads that real cores.


# Conclusion

Disable ht when there's heavy CPU load in your Kubernetes cluster?
