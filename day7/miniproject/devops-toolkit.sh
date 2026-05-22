#!/bin/bash

echo "===== DEVOPS TOOLKIT ====="

echo ""
echo "Current User:"
whoami

echo ""
echo "Hostname:"
hostname

echo ""
echo "IP Address:"
hostname -I

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "System Uptime:"
uptime

echo ""
echo "Saving output to log file..."

date >> system-report.log

echo "Toolkit execution completed."
