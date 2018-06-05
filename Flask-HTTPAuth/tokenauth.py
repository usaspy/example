from flask import Flask,make_response,jsonify,g
from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    'secret-token-1':'zhanghong',
    'secret-token-2':'lulu'
}

@auth.verify_token
def verify_token(token):
    g.user = None
    print(token)
    if token in tokens:
        g.user = tokens[token]
        return True
    return False

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error':'认证失败！'}),401)

@app.route('/')
@auth.login_required
def index():
    return "hello,%s"% g.user

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1194)