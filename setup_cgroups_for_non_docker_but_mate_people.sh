#!/bin/bash
test -d /sys/fs/cgroup/cpu,cpuacct/cpu-quota-test || sudo mkdir /sys/fs/cgroup/cpu,cpuacct/cpu-quota-test
echo "200000" | sudo tee /sys/fs/cgroup/cpu,cpuacct/cpu-quota-test/cpu.cfs_quota_us
echo "100000" | sudo tee /sys/fs/cgroup/cpu,cpuacct/cpu-quota-test/cpu.cfs_period_us
echo $PPID | sudo tee /sys/fs/cgroup/cpu,cpuacct/cpu-quota-test/tasks
echo "Start the test in this shell!"
