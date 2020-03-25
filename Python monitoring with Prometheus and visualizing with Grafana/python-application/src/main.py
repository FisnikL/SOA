import prometheus_client
from prometheus_client import Summary, Counter, Histogram, Gauge
import time
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

_INF = float("inf")

graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))


@app.get("/", response_class=PlainTextResponse)
def hello():
    start = time.time()
    graphs['c'].inc()

    time.sleep(0.600)
    end = time.time()
    graphs['h'].observe(end - start)
    return "Hello World!"


@app.get("/metrics", response_class=PlainTextResponse)
def requests_count():
    res = []
    for k, v in graphs.items():
        res.append(prometheus_client.generate_latest(v).decode("utf-8"))

    return ''.join(res)





