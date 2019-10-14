# coding=utf-8
from sqlalchemy_utils.types.choice import ChoiceType
from . import db


class Auth(object):

    def __init__(self):
        pass


class Myblog_list(db.Model):

    __table_name__ = 'myblog_list'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    like_number = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=1)
    author = db.Column(db.String(64), nullable=False)
    img = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # return '<%r>' % self.category
        return '%r' % [item for item in self.articleclass["Choice"]]


class Myblog_read(db.Model):

    __table_name__ = 'myblog_list'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    like_number = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=1)
    author = db.Column(db.String(64), nullable=False)
    beginning = db.Column(db.String(64), nullable=False)
    image = db.Column(db.String(512), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # return '<%r>' % self.category
        return '%r' % [item for item in self.articleclass["Choice"]]


class Top_list(db.Model):

    __table_name__ = 'toparticle'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    article_id = db.Column(db.Integer, nullable=False, default=1)
    create_time = db.Column(db.DateTime, nullable=False)
    expire_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)

    def __str__(self):
        return '%r' % self.category_id


class Us_prama(db.Model):

    __table_name__ = 'us_prama'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    actor = db.Column(db.String(128), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)
    plot = db.Column(db.Text, nullable=False)
    createtime = db.Column(db.DateTime, nullable=False)
    updatetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '%r' % [item for item in self.articleclass["Choice"]]


class Article_class(db.Model):

    __table_name__ = 'article_class'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    article_id = db.Column(db.Integer, nullable=False, default=1)
    category_id = db.Column(db.Integer, nullable=False, default=1)

    def __str__(self):
        return '%r' % self.category_id
