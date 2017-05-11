# -*- encoding:utf-8 -*-

"""
CloudTera
"""

from flask import Flask
from flask import abort
from flask import json
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import base64
import datetime
import flask
import logging
import os
import re
import sys
import time

app = Flask(__name__)

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

reload(sys)
sys.setdefaultencoding('utf8')


def logger(prefix):
    """
    Wall Clocks
    """
    def real_decorator(fn):
        """
        the real decorator
        """
        from functools import wraps
        # http://stackoverflow.com/a/309000/1498303
        @wraps(fn)
        def wrapper(*args, **kwargs):
            """
            the wrapper
            """
            # time.time() returns the time in seconds since the epoch as a floating point number
            start_timestamp = long(time.time() * 1000) # ms
            result = fn(*args, **kwargs)
            end_timestamp = long(time.time() * 1000)
            app.logger.info(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                            + ' ' + prefix + ' ' + str(end_timestamp - start_timestamp) + ' ms @ ' + fn.__name__)
            return result
        return wrapper
    return real_decorator


@app.route('/')
@logger('request')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 7119, debug = True)
