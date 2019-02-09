#!/usr/bin/env bash

# configure path to include our custom commands
PATH=$PATH:$(pwd)/.Secret/Commands

# make these files confidential
chmod -r Mystery/Chapter_1/SIPD/Computer/police_report.txt
