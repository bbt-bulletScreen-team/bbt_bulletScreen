from config import db
import datetime
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from automaton import automaton

conn = mysql.connector.connect(host=db['host'], user=db['user'], passwd=db['passwd'], database=db['database'], charset='utf8mb4')
db=conn.cursor()
def findUser(phone):
    db.execute('select * from b_screen where `phone`=%s', (phone,))
    result = db.fetchone()
    return result

def userLogin(phone, password):
    db.execute('select * from b_screen where `phone`=%s', (phone, ))
    result = db.fetchone()
    if result:
        if checkPwd(password, result[2]):
            return result
    return None

def createUser(phone, password,nickname):
    password = encrypt(password)
    db.execute('insert into b_screen (`phone`, `password`,`nickname`) values (%s, %s, %s)', (phone, password,nickname))
    conn.commit()
    return db.rowcount


def checkPhone(phone):
    db.execute('select * from b_screen where `phone`=%s',(phone,))
    result = db.fetchone()
    uniqueness=(result==None)
    phoneLength=((len(phone)==11) and phone[0]=='1')
    if(uniqueness and phoneLength):
    	return True
    else:
    	return False
    
def BulletProcess(phone,content):
	db.execute('select * from b_screen where `phone`=%s',(phone,))
	result=db.fetchone()
	userid=result[0]
	time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	db.execute('insert into c_bullet (`time`, `content`,`userid`) values (%s, %s, %s)', (time,content,userid))
	ContentProcessed=automaton(content)
	return ContentProcessed

def encrypt(passwd):
    return generate_password_hash(passwd)
def checkPwd(pwd, hashedPwd):
    return check_password_hash(hashedPwd, pwd)