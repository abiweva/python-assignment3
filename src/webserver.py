from datetime import datetime, timedelta
from flask import Flask, request
from flask.helpers import make_response
from flask.json import jsonify
import jwt
from sqlalchemy.orm import session
import tablecreating


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.username == tablecreating.login and auth.password == tablecreating.password:
        login.token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return '''{}'''.format(login.token)
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})
    

@app.route('/protected')
def protected():
    token = request.args.get('token')
    protected.tokenvalue = '''{}'''.format(token)
    login.token = '''{}'''.format(login.token)
    if login.token == protected.tokenvalue:
        return '''<h1>The token value is: {}'''.format(token)



if __name__ == '__main__':
    app.run(debug=True)