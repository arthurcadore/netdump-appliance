import os
import subprocess
import time

# Diretório contendo os arquivos .nfcapd originais
raw_dir = '/data/raw'
# Diretório onde os arquivos .csv convertidos serão salvos
csv_dir = '/data/csv'

# Crie o diretório .csv se ele não existir
os.makedirs(csv_dir, exist_ok=True)

# Função para converter arquivos .nfcapd para .csv
def convert_to_csv(file_path):
    # Extrair o timestamp do nome do arquivo original
    timestamp = os.path.basename(file_path).split('.')[1]
    # Caminho para o arquivo .csv convertido
    csv_file = os.path.join(csv_dir, f'{timestamp}.csv')
    if not os.path.exists(csv_file):
        # Converter o arquivo .nfcapd para .csv usando nfdump
        with open(csv_file, 'w') as f:
            subprocess.run(['nfdump', '-r', file_path, '-o', 'csv'], stdout=f)
        print(f'Converted {file_path} to {csv_file}')

        # Remover a parte indesejada do arquivo .csv
        with open(csv_file, 'r') as f:
            lines = f.readlines()
        with open(csv_file, 'w') as f:
            for line in lines:
                if line.strip() == 'Summary':
                    break
                f.write(line)

    # Excluir o arquivo .nfcapd original
    os.remove(file_path)
    print(f'Deleted original file {file_path}')

# Loop infinito para verificar periodicamente novos arquivos
while True:
    # Iterar sobre os arquivos no diretório .raw
    for file_name in os.listdir(raw_dir):
        if file_name.startswith('nfcapd.') and 'current' not in file_name:
            file_path = os.path.join(raw_dir, file_name)
            convert_to_csv(file_path)

    # Aguarde 30 segundos antes de verificar novamente
    time.sleep(30)
