from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hashirama@localhost/ass6python'
db = SQLAlchemy(app)


engine = create_engine('postgresql://postgres:hashirama@localhost/ass6python')


class Usser(db.Model):
    __tablename__ = 'usser'
    usserid = db.Column('usserid', db.Integer, primary_key=True)
    login = db.Column('login', db.Unicode)
    password = db.Column('password', db.Unicode)
    token = db.Column('token', db.Unicode)


    def __init__(self,usserid,login,password, token):
        self.usserid = usserid
        self.login = login
        self.password = password
        self.token = token


    loginn = ''
    passwordd = ''

    def tablefunc(id):
        with engine.connect() as connection:
            result = connection.execute(text("select login, password from usser where usser.usserid = "+str(id)))
            for row in result:
                global loginn, passwordd
                loginn = row['login']
                passwordd = row['password']
        connection.close()


#db.create_all()

#new_inf = Usser(1,'harakiriboy','mypassword', 'harakiriboytoken') 
#db.session.add(new_inf)
#db.session.commit()





