from app import *
from flask import request, session
from database import addBullet,findUser
from ACMachine import *
import datetime
import json

ws_pool = []
sockets=Sockets(app)
@sockets.route('/Bullet',methods=['GET'])
def echo_socket(ws):
    ws_pool.append(ws)
    for e in ws_pool:
            try:
                e.send("hello")
            except:
                ws_pool.remove(e)
    while not ws.closed:
        data = json.loads(ws.receive())
        phone=data['phone']
        message=data['message']
        existance=findUser(phone)
        if existance:
            revisedMessage=bulletCheck(message)
            rowcount=addBullet(revisedMessage,phone,)
            if(rowcount>0):
                for e in ws_pool:
                    e.send(json.dumps({'phone': phone, 'data':revisedMessage}))
            else:ws.send(json.dumps({'errcode':1,'errmsg':"请检查网络连接或其他配置"}))
        else:ws.send(json.dumps({'errcode':1,'errmsg':"该手机号未经注册"}))
        

