from tornado.ioloop import IOLoop 
from tornado.web import Application,RequestHandler
from tornado.websocket import WebSocketHandler
from tornado.options import define, options
from tornado.httpserver import HTTPServer
from database import userLogin,createUser,findUser
import datetime
import json





define("port", default=8080, help="run on the given port", type=int)

'''class IndexHandler(RequestHandler):
	def get(self):
		self.render("xxx.html")
'''





class ConnectHandler(WebSocketHandler):
	def check_origin(self,origin):
		return True

	def open(self):
		

	def on_close(self,message):
		

	def on_message(self,message):
		bullet=json.loads
		content=bullet['message']
		phone=bullet['phone']

class Login(RequestHandler):
	def post(self,*args,**kwargs):
		if self.request.headers['Content-Type'] == 'application/x-json':
			data=json.loads(self.request.body)
			phone=data['phone']
			password=data['password']
			result=userLogin(phone,password)
			if result:
				msg={'errcode':0,'errmsg':'登录成功'}
			else:
				msg={'errcode':1,'errmsg':'密码错误或用户不存在'}
			self.write(json.dumps(msg))

class Regist(RequestHandler):
	def post(self,*args,**kwargs):
		if self.request.headers['Content-Type'] == 'application/json':
			data=json.loads(self.request.body)
			phone=data['phone']
			password=data['password']
			nickname=data['nick_name']
			result=findUser(phone)
			if result:
				msg={'errcode':1,'errmsg':'手机号已被注册！'}
			elif(result==checkPhone(phone)):
				msg={'errcode':1,'errmsg':'请输入正确的手机号！'}
			else:
				result=createUser(phone,password,nickname)
				if result:
					msg={'errcode':0,'errmsg':'注册成功！'}
			self.write(json.dumps(msg))



class App(Application):
	def __init__(self):
		handlers=[
		(r'/Login',Login),
		(r'/Regist',Regist),
		(r'/Bullet',ConnectHandler)
		]
		Application.__init__(self,handlers)


if __name__=="__main__":
	options.parse_command_line()
	app=App()
	server=HTTPServer(app)
	server.listen(options.port)
	IOLoop.current().start()

