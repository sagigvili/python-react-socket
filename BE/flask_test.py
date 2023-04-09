import threading
import time
import json
import flask
from flask_cors import CORS
from flask_sock import Sock
from gevent.pywsgi import WSGIServer
from gevent import monkey

app = flask.Flask(__name__)
sock = Sock(app)
CORS(app)

value = {
    "Count": "0"
}


def heavy_func():
    global value
    while True:
        time.sleep(2)
        next = str(int(value["Count"]) + 1)
        value["Count"] = next

@app.route('/count')
def print_count():
    global value
    return value


@sock.route('/echo')
def echo(sock):
    global value
    while True:
        time.sleep(2)
        sock.send(json.dumps(value))


if __name__ == '__main__':
    monkey.patch_all()
    thread = threading.Thread(target=heavy_func)
    thread.daemon = True
    thread.start()
    #app.run() Used without waitress for dev mode
    http_server = WSGIServer(('127.0.0.1', 5000), app) # keyfile='server.key', certfile='server.crt' attributes for HTTPS
    print("Prod Server Initiated")
    http_server.serve_forever()
