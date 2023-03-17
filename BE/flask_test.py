import threading
import time
import json
import flask
from flask_cors import CORS
from flask_sock import Sock


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


@sock.route('/echo')
def echo(sock):
    global value
    while True:
        time.sleep(2)
        sock.send(json.dumps(value))


if __name__ == '__main__':
    thread = threading.Thread(target=heavy_func)
    thread.daemon = True
    thread.start()
    app.run()
