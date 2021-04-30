import time

import requests
from prometheus_client import start_http_server, Histogram

API_URL = 'http://localhost:5000'


class PrometheusConfig:
    def __init__(self):
        self.bitcoin_cost = Histogram(
            name='bitcoin_cost',
            documentation='bitcoin cost over time',
            buckets=[
                10000,
                15000,
                20000,
                25000,
                30000,
                35000,
                40000,
                45000,
                50000,
                55000,
                60000,
                65000,
                70000,
                75000,
                80000,
                85000,
                90000,
                95000,
                100000
            ],
            labelnames=['currency']
        )
        start_http_server(8000)
        self.gather_metrics()

    def gather_metrics(self):
        while True:
            json_response = requests.get(API_URL).json()
            for currency, price in json_response.items():
                self.bitcoin_cost.labels(currency).observe(float(''.join(price.split(','))))
            time.sleep(5)


if __name__ == '__main__':
    print('Prometheus server starting at: http://localhost:8000')
    PrometheusConfig()
