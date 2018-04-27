#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, Response
import time
import urllib3
from json import loads

BLOWOUT_API_ENDPOINT = 'http://127.0.0.1:5000/api/info'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/progress')
def progress():

    def generate():
        x = 0
        http = urllib3.PoolManager()
        while x <= 100:
            response = http.request('GET', BLOWOUT_API_ENDPOINT)
            payload = response.data.decode('utf-8')
            srv_info = loads(payload)
            x = srv_info['current_weight']
            yield "data:" + str(x) + "\n\n"
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True)

			
