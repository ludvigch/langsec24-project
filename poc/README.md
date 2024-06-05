
# Instructions for pydash 5.1.2 and flask PoC

**Prerequisites:** python3.x, pip

## Setup vulnerable python package

* **Create a python virtualenv if you don't want to taint your python installation with vulnerable packages, for example:**
    1. python3 -m venv env
    2. source /env/bin/activate
    3. pip install -r requirements.txt 

## pydash 5.1.2 PoC

* **Run the proof of concept**
    1. python3 pydash_poc_5.1.2.py

## flask PoC

* **Run flask proof of concept**
    1. flask --debug --app flask_poc.py run
    2. Open browser and enter following url: <http://127.0.0.1:5000/?path=__class__.__init__.__globals__.app.secret_key&val='1337'>
    3. result will be printed in the terminal window running the flask server

## Latest pydash Poc

* **Install latest pydash release**
    1. pip install pydash
* **Run the PoC**
    1. python3 pydash_poc_latest.py
