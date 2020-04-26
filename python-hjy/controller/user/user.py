from app import app
from flask import request, session
from database import createUser, userLogin,checkPhone

@app.route('/web/regist', methods=['POST'])
def register():
    data = request.get_json()
    phone=data['phone']
    nick_name = data['nick_name']
    password = data['password']
    
    result = checkPhone(phone)
    if (result['phoneLength']==True):
        if(result['uniqueness']==False):
            return {
            'errcode': 400,
            'errmsg': '该手机已被填写'
            }, 400
    elif(result['phoneLength']==False):
        return{
            'errcode': 400,
            'errmsg': '手机号格式不正确'
            }, 400
    
    rowcount = createUser(nick_name,phone,password)
    if rowcount > 0:
        return {
            'errcode': 0,
            'errmsg': '注册成功'
        }, 200
    
    return {
        'errcode': 400,
        'errmsg': '请检查网络或其他设置'
    }, 400

@app.route('/web/login', methods=['POST'])
def login():
    data = request.get_json()
    phone=data['phone']
    password = data['password']

    result = userLogin(phone, password)
    
    if result:
        session['user_id'] = result[0]
        uName=getUser(session['user_id'])
        return {
            'errcode': 0,
            'errmsg': '登陆成功',
        }, 200
    
    return {
        'errcode': 401,
        'errmsg': '用户不存在或密码错误'
    }, 401
