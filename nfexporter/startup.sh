#!/bin/bash

DB_HOST="database"
DB_USER="pythonConnector"
DB_PASSWORD="Python@connect123"

while ! mysqladmin ping -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" --silent; do
    echo "Waiting for database be ready..."
    sleep 1
done

echo "The Database is ready!"

python3 /data/nf2csv.py & 

python3 /data/csv2db.py