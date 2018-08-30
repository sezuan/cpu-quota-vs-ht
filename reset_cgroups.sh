#!/bin/bash
for i in `cat /sys/fs/cgroup/cpu,cpuacct/cpu-quota-test/tasks`; do echo $i | sudo tee /sys/fs/cgroup/cpu,cpuacct/tasks;done
