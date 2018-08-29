#!/usr/bin/env python3

import sys
import time
import psutil
import signal
from pbkdf2 import PBKDF2
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value

def signal_handler(sig, frame):
    finish()

def finish():
    [X.terminate() for X in procs]
    [X.join() for X in procs]
    try:
        sys.exit(0)
    except:
        pass

def do(lock, num_procs, terminate, iterations,requests):
    with num_procs.get_lock():
       num_procs.value += 1

    while True:

        start = time.perf_counter()
        start_cpu = time.process_time()
        PBKDF2("was","was",iterations=iterations).read(64)
        end = time.perf_counter()
        end_cpu = time.process_time()
        rate=1/(end-start)
        with requests.get_lock():
            requests.value += 1

        if requests.value % 10 == 0:
            with lock:
                if terminate.value == 0:
                    print("%s\t%0.1f\t%0.1f\t%0.1f\t%0.1f" % (
                        num_procs.value,
                        psutil.cpu_percent(),
                        (end_cpu - start_cpu)*1000,
                        (end-start)*1000,
                        rate))
    
    num_procs.value -= 1

signal.signal(signal.SIGINT, signal_handler)

procs = []
lock = Lock()
num_procs = Value('i', 0, lock = True)
requests = Value('i', 0, lock = True)
terminate = Value('i', 0, lock = True)

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("... <num_of_parallel_procs> [<iterations>(default: 2000)]")
    sys.exit(0)

if len(sys.argv) == 3:
    iterations = int(sys.argv[2])
else:
    iterations = 2000

num_parallel_procs = int(sys.argv[1])

for i in range(num_parallel_procs):
    if num_procs.value < num_parallel_procs:
        p = Process(target=do, args=(lock,num_procs,terminate,iterations,requests))
        p.start()
        procs.append(p)

time.sleep(1)
start = time.perf_counter()
r1 = requests.value
time.sleep(4)
end = time.perf_counter()
r2 = requests.value
rate = (r2-r1)/(end-start)
terminate.value = 1
with lock:
    print("*** procs: %2i rate:  %0.1f ***" % (num_procs.value, rate))

finish()
