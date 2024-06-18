#!/bin/bash

NETFLOW_DIR="/var/log/netflow"
CSV_DIR="/var/log/netflow/csv"
NETFLOW_PORT=2005

mkdir -p $NETFLOW_DIR
mkdir -p $CSV_DIR

nfcapd -w -D -p $NETFLOW_PORT -l $NETFLOW_DIR

convert_to_csv() {
    for file in $NETFLOW_DIR/nfcapd.*; do
        if [[ -f $file ]]; then
            timestamp=$(basename $file | cut -d'.' -f2-)
            csv_file="$CSV_DIR/netflow_$timestamp.csv"
            if [[ ! -f $csv_file ]]; then
                nfdump -r $file -o csv > $csv_file
                echo "Converted $file to $csv_file"
            fi
        fi
    done
}

while true; do
    convert_to_csv
    sleep 30
done
