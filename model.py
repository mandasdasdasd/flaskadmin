# coding=utf-8
from . import db
from flask import request


class Auth(object):

    def __init__(self):
        pass
    def get_token(self):
        cookie = request.cookies
        token = cookie.get("token")
        return token


class Myblog_list(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    like = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(64), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
