FROM netsage/nfdump-collector:alpine-1.6.23

COPY nfdump/startup.sh /usr/sbin/startup.sh
RUN chmod +x /usr/sbin/startup.sh

CMD ["/usr/sbin/startup.sh"]