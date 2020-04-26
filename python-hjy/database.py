from config import db
import mysql.connector
from utils import encrypt, checkPwd

conn = mysql.connector.connect(host=db['host'], user=db['user'], passwd=db['passwd'], 
                                database=db['database'], charset='utf8mb4')
db = conn.cursor()

def findUser(phone):
    db.execute('select * from users where `phone`=%s', (phone,))
    result = db.fetchall()
    return result

def userLogin(phone, password):
    db.execute('select * from users where `phone`=%s', (phone,))
    result = db.fetchone()
    if result:
        if checkPwd(password, result[3]):
            return result
    return None

def createUser(nick_name,phone,password):
    password = encrypt(password)
    db.execute('insert into users (`nick_name`,`phone` ,`password`) values (%s, %s, %s)', (nick_name,phone,password))
    conn.commit()
    return db.rowcount

def addBullet(message,phone):
    db.execute('insert into bullet ( `message`,`phone`) values (%s, %s)', (message,phone))
    conn.commit()
    return db.rowcount

def getUser(anId):
    db.execute('select * from users where `id`= %s',(anId,))
    finalGot=db.fetchone()
    return finalGot[1]


def checkPhone(phone):
    db.execute('select * from users where `phone`=%s',(phone,))
    result = db.fetchone()
    dictReturn=dict()
    uniqueness=(result==None)
    phoneLength=((len(phone)==11)and phone[0]=='1')
    return {
        'phoneLength':phoneLength,
        'uniqueness':uniqueness}
