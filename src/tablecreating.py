from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hashirama@localhost/ass6python'
db = SQLAlchemy(app)



class Usser(db.Model):
    __tablename__ = 'usser'
    usserid = db.Column('usserid', db.Integer, primary_key=True)
    login = db.Column('login', db.Unicode)
    password = db.Column ('password', db.Unicode)
    def __init__(self,usserid,login,password):
        self.usserid = usserid
        self.login = login
        self.password = password


#db.create_all()

#new_inf = Usser(5,'harakirigirl','herpassword')
#db.session.add(new_inf)
#db.session.commit()


login = ''
password = ''

engine = create_engine('postgresql://postgres:hashirama@localhost/ass6python')
with engine.connect() as connection:
    result = connection.execute(text("select login, password from usser where usser.usserid = 1"))
    for row in result:
        login =  row['login']
        password = row['password']


connection.close()
