import os
import csv
import mysql.connector
import time

db_config = {
    'host': 'database',
    'user': 'pythonConnector',
    'password': 'Python@connect123',
    'database': 'netflow'
}

csv_dir = '/data/csv'

def import_csv_to_mysql(file_path, cursor):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        headers = next(csv_reader) 

        if len(headers) != 48:
            print(f'Header column count mismatch: {len(headers)} columns found. Expected 48.')
            return

        for row in csv_reader:
            if len(row) == 48:
                try:
                    query = '''
                        INSERT INTO tabela_netflow (
                            ts, te, td, sa, da, sp, dp, pr, flg, fwd, stos, ipkt, ibyt, opkt, obyt,
                            inbound, outbound, sas, das, smk, dmk, dtos, dir, nh, nhb, svln, dvln, ismc, odmc,
                            idmc, osmc, mpls1, mpls2, mpls3, mpls4, mpls5, mpls6, mpls7, mpls8, mpls9,
                            mpls10, cl, sl, al, ra, eng, exid, tr
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    '''
                    cursor.execute(query, tuple(row))
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
            else:
                print(f'Skipping row with incorrect number of columns: {len(row)} columns found. Expected 48. Row: {row}')
    print(f'Imported {file_path} to MySQL and deleted the original file.')
    os.remove(file_path)

while True:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    for file_name in os.listdir(csv_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(csv_dir, file_name)
            import_csv_to_mysql(file_path, cursor)

    conn.commit()
    cursor.close()
    conn.close()
    
    time.sleep(30)
