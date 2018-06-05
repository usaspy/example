
from flask import Flask,render_template
from huawa.db import queryOrder


app = Flask(__name__)

@app.route('/')
def view():
    return render_template('vieworder.html',counts=queryOrder())

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=80)