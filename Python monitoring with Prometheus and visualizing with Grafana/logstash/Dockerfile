  
FROM docker.elastic.co/logstash/logstash:7.6.1

RUN mkdir /usr/share/logstash/custom_patterns

CMD ["-f", "/usr/share/logstash/pipeline/logstash.conf", "-r"]