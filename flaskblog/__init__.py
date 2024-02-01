import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app=Flask(__name__)
app.config['SECRET_KEY']='d74680c7dd28ba85b126fd4c10f684a8'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('ishanthari96@gmail.com')
app.config['MAIL_PASSWORD']=os.environ.get('oppo33')
mail=Mail(app)

with app.app_context():
    # Create all database tables
    print ('h')
    db.create_all()

from flaskblog import routes