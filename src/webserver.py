from datetime import datetime, timedelta
from re import U
from flask import Flask, request                 # importing required modules and libraries
from flask.helpers import make_response
import jwt
from sqlalchemy.orm import session
import tablecreating                     # import tablecreating in order to have access to vars and methods inside tablecreating.py file


app = tablecreating.app                                  #create app var to store there already created Flask app webserver starter
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'        #identify configuration for app inside this file
 

@app.route('/login')
def login():                               
    auth = request.authorization
    myid = 3                           #creating id variable as parameter for tablefunc method for identify as which user we want to login
    tablecreating.Usser.tablefunc(myid)
    if auth and auth.username == tablecreating.loginn and auth.password == tablecreating.passwordd:  # if statement to verificate are the data form database is identical with data that we input 
        login.token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])  # encoding unique token for logged user
        
        update_this =   tablecreating.Usser.query.filter_by(usserid=myid).first()  
        update_this.token = '''{}'''.format(login.token)                              # this block of code used for updating users existing token with new encoded token inside the correct row in database 
        tablecreating.db.session.commit()
        
        return "token: " + '''{}'''.format(login.token)    # getting user's token in html page
    return make_response('Could not found a user with login: ' + tablecreating.loginn, 401, {'WWW-Authenticate': 'Basic realm="Login required'})  #make response that login not found if our statement will be false
    

@app.route('/protected')
def protected():                               # protected method for verificate the equalness of our tokens
    token = request.args.get('token')                 # store token value inside token variable
    protected.tokenvalue = '''{}'''.format(token)         # store value of token as string inside tokenvalue and right before it protected keyword to locate between methods
    login.token = '''{}'''.format(login.token)         # store inside login.token var the value of login.token from login method
    if login.token == protected.tokenvalue:                                # if statement to check the correctness
        return '<h1>Hello, token which is provided is correct </h1>'     # if it is correct this will semd us msg that token is correct
    else:
        return '<h1>Hello, Could not verify the token </h1>'    # vice versa with insode 'else'



if __name__ == '__main__':     # used for running our code
    app.run(debug=True)
