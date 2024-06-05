Prerequisites: python3.x, pip
* create a python virtualenv if you don't want to taint your python installation with vulnerable packages, for example:
    1. python3 -m venv env
    2. source /env/bin/activate
* install vulnerable packages in the environment
    1. pip install -r requirements.txt 
* run the proof of concept
    1. python3 pydash_poc_5.1.2.py
