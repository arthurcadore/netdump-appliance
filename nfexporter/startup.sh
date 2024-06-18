#!/bin/bash

DB_HOST="database"
DB_USER="pythonConnector"
DB_PASSWORD="Python@connect123"

while ! mysqladmin ping -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" --silent; do
    echo "Aguardando o banco de dados estar pronto..."
    sleep 1
done

echo "O banco de dados está pronto para aceitar consultas."

python3 /data/nf2csv.py & 

python3 /data/csv2db.py & 

tail -f /dev/null 
