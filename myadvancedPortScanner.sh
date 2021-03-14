#!/bin/bash

#advacned MYSQL port scanner

echo "enter first IP address:"
read FirstIP

echo "enter last octate of IP address:"
read lastOctIP

echo "enter the port number you want to scan for:"
read port


nmap -sT $FirstIP-$lastOctIP -p $port >/dev/null -oG MYSQLscan

cat MYSQLscan | grep open > MYSQLscan2

cat MYSQLscan2


