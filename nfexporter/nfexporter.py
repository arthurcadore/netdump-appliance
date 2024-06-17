import MySQLdb
import nfdump

def process_packet(packet):
  # Configuração da conexão com o MySQL
  db = MySQLdb.connect(host="database", user="pythonConnector", passwd="Python@connect123", database="netflow")
  cursor = db.cursor()

  # Extrair dados relevantes do fluxo Netflow
  timestamp = packet.timestamp
  src_ip = packet.src_ip
  dst_ip = packet.dst_ip
  proto = packet.protocol
  packets = packet.packets
  bytes = packet.bytes
  duration = packet.duration

  # Preparar a consulta SQL para inserir os dados na tabela
  dados = (timestamp, src_ip, dst_ip, proto, packets, bytes, duration)
  sql = """
  INSERT INTO `tabela_netflow`
  (`timestamp`, `src_ip`, `dst_ip`, `proto`, `packets`, `bytes`, `duration`)
  VALUES (%s, %s, %s, %s, %s, %s, %s)
  """

  # Executar a consulta SQL
  cursor.execute(sql, dados)

  # Confirmar as alterações no banco de dados
  db.commit()

  # Fechar o banco de dados
  db.close()

def main():
  # Abrir o socket Nfdump
  with nfdump.open() as reader:
    # Processar cada pacote Netflow
    for packet in reader:
      process_packet(packet)

if __name__ == "__main__":
  main()