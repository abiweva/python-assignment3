# this tablecreating.py file is created to produce required table in postgresql database to store user data in there 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql    #importing required libraries and modules
from sqlalchemy.sql import text
from sqlalchemy import create_engine


app = Flask(__name__)        #creating the app var to start Flask web server
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hashirama@localhost/ass6python'  #adding sqlalchemy database config to connect server with my postgresql
db = SQLAlchemy(app)   #creating db var to do sql actions via this var


engine = create_engine('postgresql://postgres:hashirama@localhost/ass6python')  # creating engine to execute select query from my database


class Usser(db.Model):             #identify class Usser as table, and Usser is tablename
    __tablename__ = 'usser'
    usserid = db.Column('usserid', db.Integer, primary_key=True)   #adding additional required queries for db table
    login = db.Column('login', db.Unicode)
    password = db.Column('password', db.Unicode)
    token = db.Column('token', db.Unicode)


    def __init__(self,usserid,login,password, token):  #defining constructor for Usser class
        self.usserid = usserid
        self.login = login
        self.password = password
        self.token = token


    loginn = ''     #creating empty login and password variables to store inside results from Usser table when selecting data
    passwordd = ''  #making their name different to make it differ from table columns to prevent errors

    def tablefunc(id):                         #creating tablefunc method to execute select query and store data inside our empty variables using engine and connect
        with engine.connect() as connection:
            result = connection.execute(text("select login, password from usser where usser.usserid = "+str(id)))
            for row in result:
                global loginn, passwordd
                loginn = row['login']
                passwordd = row['password']
        connection.close()                        #always close the connection


#-------------------------------------------------------------------------------------
#db.create_all()                            # this block of code commented because you must use this only once, because it will make error when you create the same table as previous

#new_inf = Usser(1,'harakiriboy','mypassword', 'harakiriboytoken')     # this block of code commented because you must insert only distinct id's inside the table 
#db.session.add(new_inf)                                               # or you can just change the inserting values                  
#db.session.commit()
#------------------------------------------------------------------------------------




