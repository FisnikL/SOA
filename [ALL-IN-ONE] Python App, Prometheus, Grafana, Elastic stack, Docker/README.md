# Logging & Monitoring

This application includes dockerized:
- Python Application
- Prometheus
- Grafana
- Elastic stack (Elasticsearch, Logstash, Kibana)


# Starting
- docker-compose up
- Then services can be accessed on:
  - Python application
    - http://localhost:81
    - http://localhost:81/metrics
  - Prometheus
    - http://localhost:9091
  - Grafana
    - http://localhost:3000
  - Elasticsearch
    - http://localhost:9200
  - Kibana
    - http://localhost:5601
  - Logstash
    - http://localhost:9600
