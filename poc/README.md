Prerequisites: python3.x, pip
1. create a python virtualenv if you don't want to taint your python installation with vulnerable packages, for example:
    1.1 python3 -m venv env
    1.2 source /env/bin/activate
2. install vulnerable packages in the environment
    2.1 pip install -r requirements.txt 
3. run the proof of concept
    3.1 python3 pydash_poc.py
