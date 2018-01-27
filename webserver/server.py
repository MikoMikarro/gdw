from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "{status: ok, message: 'GDW SERVER'}"

@app.route("/volume/", methods=['POST'])
def volume():
    if request.method == "POST":
        volume = request.form['volume']
        print volume
        return "{status: ok, message: 'Volume set to" + volume + "'}"
