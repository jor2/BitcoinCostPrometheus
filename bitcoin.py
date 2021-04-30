import requests
from flask import Flask, jsonify

app = Flask(__name__)

COINDESK_API = 'https://api.coindesk.com/v1/bpi/currentprice.json'


class BitcoinIndex:
    def __init__(self):
        self.json_response = self.request_prices

    def calculate_prices(self):
        self.set_json_response()
        self.bitcoin_euro()
        self.bitcoin_usd()
        self.bitcoin_gbp()

    @property
    def request_prices(self):
        return requests.get(COINDESK_API).json()

    def set_json_response(self):
        self.json_response = self.request_prices

    @property
    def bitcoin_euro(self):
        return self.json_response['bpi']['EUR']['rate']

    @property
    def bitcoin_usd(self):
        return self.json_response['bpi']['USD']['rate']

    @property
    def bitcoin_gbp(self):
        return self.json_response['bpi']['GBP']['rate']

    @property
    def get_prices_json(self):
        d = {}
        for currency, info in self.json_response['bpi'].items():
            d[currency] = info['rate']
        return jsonify(d)


@app.route('/')
def prices():
    return BitcoinIndex().get_prices_json


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
