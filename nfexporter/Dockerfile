
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y nfdump net-tools && \
    apt-get clean

COPY nfexporter.sh /usr/local/bin/nfexporter.sh
RUN chmod +x /usr/local/bin/nfexporter.sh

CMD ["sh", "-c", "/usr/local/bin/nfexporter.sh"]