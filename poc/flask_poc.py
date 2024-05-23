import pydash
from flask import Flask, request

app = Flask(__name__)
app.secret_key = "secret value"

class User():
    def __init__(self):
        pass

@app.route("/")
def poc():
    print("secret_key before: "+app.secret_key)
    user = User()
    path = request.args.get('path')
    value = request.args.get('val')
    print(user.__class__.__init__.__globals__['app'].secret_key)
    user.__class__.__init__.__globals__['app'].secret_key = "1337"
    if value != None or path != None:
        pydash.set_(user, path, value)
    else:
        return "you need to specify /?path=<path to edit>&value=<value to edit>"
    print("secret_key after: "+app.secret_key)
    return "you queried: /"