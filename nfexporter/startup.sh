#!/bin/bash

python3 /data/nf2csv.py & 

python3 /data/csv2db.py & 

tail -f /dev/null 
