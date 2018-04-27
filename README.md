# Description
This is a small api server that if called via a REST api, will add to an internal "weight" (initially set to 0)

Weight is always added with a predefined increment (default = 1).

Once the server has reached "max" value (default = 100), it runs a "blowout" routine and resets.
'

## Installation

pip install -r src/requirements.txt

## run the server

./server.py

## Test with curl

1. To look at current status:
curl -i <http://yourip:5000/api/info

2. To add weight to the server:
curl -i <http://yourip:5000/api/add

In case you have reached "blowout" state (Winner!) blowout is set to True.
The server will then run the "blowout" code.