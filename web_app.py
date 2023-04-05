import gc
import logging
import random

from waitress import serve
from flask import Flask


# hello_string = "Hello"
app = Flask(__name__)


@app.route("/index")
def hello():
    return "Hello"


# Random generation 1000 and return sum of them all
@app.route("/moreload")
def moreload():
    x = [random.randrange(1, 10, 1) for _ in range(1000)]
    sum_all_str = str(sum(x))
    del x
    return sum_all_str


if __name__ == "__main__":
    # gc.enable()
    # logging.getLogger('werkzeug').disabled = True
    # log = logging.getLogger('werkzeug')
    # log.disabled = True
    # app.run(host='0.0.0.0', debug=False
    serve(app, listen='*:5000', connection_limit=5000, threads=4)




