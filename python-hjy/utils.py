from werkzeug.security import generate_password_hash, check_password_hash

def encrypt(passwd):
    return generate_password_hash(passwd)

def checkPwd(pwd, hashedPwd):
    return check_password_hash(hashedPwd, pwd)
