# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


app = Flask(__name__, template_folder='templates')
db = SQLAlchemy(app)


from view import Login, TestModel
from model import Myblog_list


def create_app():
    admin = Admin(app, name='MyAdmin', template_mode='bootstrap3')

    app.config['SECRET_KEY'] = '123456'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ysman:123456@47.93.187.111:3306/myblog'

    admin.add_view(TestModel(Myblog_list, db.session))
    admin.add_view(Login(name='test', endpoint='index'))

    return app
