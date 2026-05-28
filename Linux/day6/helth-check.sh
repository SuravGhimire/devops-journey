#!/bin/bash

echo "=== SYSTEM HEALTH CHECK ==="

echo ""

echo "Current User: "
whoami

echo ""
echo "disk usage "
df -h

echo ""
echo "Memory Usage: "
free -h

echo ""
echo "System Uptime:"
uptime

