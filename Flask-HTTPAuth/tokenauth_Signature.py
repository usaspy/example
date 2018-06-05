from flask import Flask,make_response,jsonify,g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
serializer = Serializer(app.config['SECRET_KEY'], expires_in=1800)


auth = HTTPTokenAuth(scheme='Bearer')

users = ['zhanghong','lulu','冬阳']

for user in users:
    token = serializer.dumps({'username': user})
    print('Token for {}: {}\n'.format(user, token))

@auth.verify_token
def verify_token(token):
    g.user = None
    print(token)
    try:
        data = serializer.load(token)
    except:
        return False
    print(data)
    if 'username' in data:
        g.user = data['username']
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