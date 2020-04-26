from flask import Flask
import mysql.connector
import config
from flask_sockets import Sockets

app = Flask(__name__)
app.config['SECRET_KEY'] = config.app['secret_key']


from controller.user.user import *
from controller.bullet.bullet import *



if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('0.0.0.0', 5002), app, handler_class=WebSocketHandler)
    print('Web server start')
    server.serve_forever()
