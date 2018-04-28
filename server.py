#!/usr/bin/env python
from flask import Flask, jsonify



__info = {
    'blowout_weight': 100,
    'increment': 1,
    'current_weight': 0,
    'blowout': False
}

info = __info


app = Flask(__name__)


@app.route('/')
def index():
    return "Online!"


# Shows basic info
@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(info)

@app.route('/api/add', methods=['GET'])
def get_add():
    """
    A call to this function will add 1*increment to the weight.
    If the caller added the last effort, 'blowout' variable is set to True.
    """

    if info['current_weight'] >= __info['blowout_weight']:
        info['blowout'] = True
        info['current_weight'] = 0
        blowout()
    else:
        info['current_weight'] += __info['increment']
        info['blowout'] = False
    return jsonify(info)
    


def blowout():
    """
    Runs whatever code needed to blowout.
    """
    print("Blowout!")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
