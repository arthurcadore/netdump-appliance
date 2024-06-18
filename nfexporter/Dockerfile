FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get clean

RUN apt-get install -y \
            nfdump \
            net-tools \
            python3-dev \
            default-libmysqlclient-dev \
            build-essential \
            pkg-config
    
RUN pip install mysqlclient

CMD ["tail -f /dev/null"]