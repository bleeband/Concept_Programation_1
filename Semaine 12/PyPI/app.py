# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! I am a Flask app running on PyPI!'

