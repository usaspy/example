from flask import Flask,make_response,jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

#users = [{'username':'zhanghong','password':'119'},{'username':'lulu','password':'123456'}]
users_hash = [{'username':'zhanghong','password':generate_password_hash('119')},{'username':'lulu','password':generate_password_hash('123456')}]

#只支持明文
#@auth.get_password
#def get_password(username):
#    for user in users:
#        if user['username'] == username:
#            return user['password']
#    return None

#支持加密的密码
@auth.verify_password
def verify_password(username,password):
    for user in users_hash:
        if user['username'] == username:
            if check_password_hash(user['password'],password):
                return True
    return False

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error':'认证失败！'}),401)

@app.route('/')
@auth.login_required
def index():
    return "hello,%s"% auth.username()

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1194)