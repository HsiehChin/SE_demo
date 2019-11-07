from flask import *
import ReplayMessage as reply
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 0


@app.route('/helloWorld')
def index():
    return str(reply.helloWorld())


@app.route('/goodMorning')
def index():
    return str(reply.helloWorld())


@app.route('/howAreYou')
def index():
    return str(reply.howAreYou())


if __name__ == '__main__':
    app.run(debug=True)