import random
import logging

import prometheus_client
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Gauge, Histogram, Summary

import logging
from logging.handlers import RotatingFileHandler
from fastapi.logger import logger as fastapi_logger

app = FastAPI()

formatter = logging.Formatter("[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s", "%Y-%m-%d %H:%M:%S")
handler = RotatingFileHandler('/app/logs/logFile.log', backupCount=0)
handler.setFormatter(formatter)
logging.getLogger().setLevel(logging.NOTSET)
fastapi_logger.addHandler(handler)

graphs = {
    'counter': Counter('python_my_counter', 'This is my counter'),
    'gauge': Gauge('python_my_gauge', 'This is my gauge'),
    'histogram': Histogram('python_my_histogram', 'This is my histogram'),
    'summary': Summary('python_my_summary', 'This is my summary')
}


@app.get("/", response_class=PlainTextResponse)
def hello(request: Request):
    graphs['counter'].inc(random.random())
    graphs['gauge'].set(random.random() * 15 - 5)
    graphs['histogram'].observe(random.random() * 10)
    graphs['summary'].observe(random.random() * 10)

    fastapi_logger.info(request.client.host + " " + request.method + " Hello World")

    return 'Hello World'


@app.get("/metrics", response_class=PlainTextResponse)
def requests_count():
    res = []
    for k, v in graphs.items():
        res.append(prometheus_client.generate_latest(v).decode("utf-8"))

    return ''.join(res)

