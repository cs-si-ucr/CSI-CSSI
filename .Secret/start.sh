#!/usr/bin/env bash

# configure path to include our custom commands
PATH=$PATH:$(pwd)/.Secret/Commands

# make these files confidential
chmod -r Mystery/Chapter_1/SIPD/Computer/police_report.txt

# Compile to here
g++ .Secret/login.cpp -o .Secret/Temp/Andre_House/Laptop/login