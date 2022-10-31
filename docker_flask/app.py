from flask import Flask, jsonify
from multiprocessing import Value
import os
import socket

counter = Value('i', 0)
app = Flask(__name__)

@app.route("/about")
def hello():
    
    html = "<h3>Hello, Polina!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route("/stat") 
def count():
    with counter.get_lock():
        counter.value += 1
        out = counter.value
    return jsonify(count=out)

@app.route("/") 
def stat():
    return jsonify(counter.value)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)