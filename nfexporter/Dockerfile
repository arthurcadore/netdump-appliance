FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get clean

RUN apt-get install -y \
            nfdump \
            net-tools \
            python3-dev \
            default-libmysqlclient-dev \
            build-essential \
            pkg-config \
            default-mysql-client 
    
RUN pip install mysqlclient

RUN pip install --no-cache-dir mysql-connector-python

RUN mkdir -p /data/csv

# Add startup script to container:
COPY nfexporter/startup.sh /usr/sbin/startup.sh
RUN chmod +x /usr/sbin/startup.sh
    
# Starts and Mantain container running:
CMD ["/usr/sbin/startup.sh"]
