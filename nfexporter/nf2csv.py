import os
import subprocess
import time

raw_dir = '/data/raw'
csv_dir = '/data/csv'

os.makedirs(csv_dir, exist_ok=True)

def convert_to_csv(file_path):
    timestamp = os.path.basename(file_path).split('.')[1]
    csv_file = os.path.join(csv_dir, f'{timestamp}.csv')
    if not os.path.exists(csv_file):
        with open(csv_file, 'w') as f:
            subprocess.run(['nfdump', '-r', file_path, '-o', 'csv'], stdout=f)
        print(f'Converted {file_path} to {csv_file}')

        with open(csv_file, 'r') as f:
            lines = f.readlines()
        with open(csv_file, 'w') as f:
            for line in lines:
                if line.strip() == 'Summary':
                    break
                f.write(line)

    os.remove(file_path)
    print(f'Deleted original file {file_path}')

while True:
    for file_name in os.listdir(raw_dir):
        if file_name.startswith('nfcapd.') and 'current' not in file_name:
            file_path = os.path.join(raw_dir, file_name)
            convert_to_csv(file_path)

    time.sleep(30)
