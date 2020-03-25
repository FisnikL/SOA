import random

import prometheus_client
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Gauge, Histogram, Summary

app = FastAPI()

_INF = float("inf")

graphs = {
    'counter': Counter('python_my_counter', 'This is my counter'),
    'gauge': Gauge('python_my_gauge', 'This is my gauge'),
    'histogram': Histogram('python_my_histogram', 'This is my histogram'),
    'summary': Summary('python_my_summary', 'This is my summary')
}


@app.get("/", response_class=PlainTextResponse)
def hello():
    graphs['counter'].inc(random.random())
    graphs['gauge'].set(random.random() * 15 - 5)
    graphs['histogram'].observe(random.random() * 10)
    graphs['summary'].observe(random.random() * 10)
    # process_request(random.random() * 5)

    return 'Hello World'


@app.get("/metrics", response_class=PlainTextResponse)
def requests_count():
    res = []
    for k, v in graphs.items():
        res.append(prometheus_client.generate_latest(v).decode("utf-8"))

    return ''.join(res)

# graphs['requests'].inc()
# r = random.randrange(5)
#
# # Successfully processed
# if r < 4:
#     graphs['successfully'].inc()
#     return "Hello World!"
# # Error, Exception
# else:
#     graphs['error'].inc()
#     return "Error"

