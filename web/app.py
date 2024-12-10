# save this as app.py
from flask import Flask

app = Flask("my web server")

@app.route("/")
def hello():
    return "Hello, World!"

app.run()