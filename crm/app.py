import hashlib
import flask
import ssl
import flask_httpauth
from passlib.apps import custom_app_context as pwd_context
from dbFactory import dbFactory
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xxqx@2017mysql!@#@116.62.164.196/CRM"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
db = SQLAlchemy(app)

auth = flask_httpauth.HTTPBasicAuth()
#基于用户名/密码的登录认证
#如果是令牌则存放在username，password为None
@auth.verify_password
def verify_password(username_or_token,password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.get(username_or_token)
        if user is None: #用户不存在
            return False
        if User.md5_password(password) != user.password_hash: #密码有误
            return False

    flask.g.user = user
    return True

@auth.error_handler
def unauthorzied():
    return flask.make_response(flask.jsonify({'error':'Unauthorized access'}),401)

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(32), primary_key = True,index = True)
    password_hash = db.Column(db.String(128)) #hash编码后存放
    sex = db.Column(db.String(32))
    age = db.Column(db.Integer)
    address = db.Column(db.String(128))

    @staticmethod
    def md5_password(password):
        m = hashlib.md5()
        m.update(password.encode(encoding="utf-8"))
        return m.hexdigest()

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'username': self.username})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['username'])

        return user

#获取令牌，第一次需要输入用户名/密码才能得到所以要加上@auth.login_required
@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = flask.g.user.generate_auth_token()
    return flask.jsonify({ 'token': token.decode('ascii') })

@app.route('/api/adduser',methods=['POST'])
@auth.login_required
def add_user():
    username = flask.request.json.get('username')
    password = flask.request.json.get('password')
    age = flask.request.json.get('age')
    sex = flask.request.json.get('sex')
    address = flask.request.json.get('address')

    if username is None or password is None:
        flask.abort(301)
    if User.query.filter_by(username=username).first() is not None:
        flask.abort(302) # 用户已存在

    user = User()
    user.username = username
    user.password_hash = User.md5_password(password)
    user.age = age
    user.sex = sex
    user.address = address

    db.session.add(user)
    db.session.commit()

    return flask.jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', username = user.username, _external = True)}

@app.route('/api/users/<string:username>',methods=['GET'])
def get_user(username): #应该用UserId
    user = User.query.get(username)
    if not user:
        flask.abort(400)
    return flask.jsonify({'username': user.username})



#------------------------------------------传统写法：dbFactory 添加新的用户-----------------------------------
@app.route('/justdoit/api/v1.0/user', methods=['POST'])
def addUser():
    username = flask.request.json.get('username')
    password = flask.request.json.get('password')
    age = flask.request.json.get('age')
    sex = flask.request.json.get('sex')
    address = flask.request.json.get('address')
    if username is None or password is None:
        print("参数不完整..")
        flask.abort(302)

    user = {
        'username': username,
        'password': pwd_context.encrypt(password),
        'sex': sex,
        'age':age,
        'address':address
    }

    sql = "insert into user(username,password,age,sex,address) values ('%s','%s','%d','%s','%s')"% (user['username'],user['password'],user['age'],user['sex'],user['address'])

    c = dbFactory("116.62.164.196", "root", "xxqx@2017mysql!@#", "CRM")
    rs = c.exeUpdate(sql)

    if rs is True:
        return  flask.jsonify({'result': 'success'})
    return flask.jsonify({'result': 'failed'})

if __name__ == '__main__':
    app.run(host='localhost',port=999,debug=True, ssl_context='adhoc')