# coding=utf-8
from sqlalchemy_utils.types.choice import ChoiceType
from . import db
TYPES = [
    (1, u'python'),
    (2, u'杂文'),
    (3, u'linux'),
    (4, u'前端'),
    (5, u'duanzi'),
    (6, u'read'),
    (7, u'美剧')
    ]


class Auth(object):

    def __init__(self):
        pass


class Myblog_list(db.Model):

    __table_name__ = 'myblog_list'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    like = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=1)
    author = db.Column(db.String(64), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    articleclass = db.relationship('Article_class', backref='articleid')  # backred 允许反向查找

    def __repr__(self):
        # return '<%r>' % self.category
        return '%r' % [item for item in self.articleclass["Choice"]]


class Article_class(db.Model):

    __table_name__ = 'article_class'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('myblog_list.id'))
    category_id = db.Column(ChoiceType(TYPES))

    def __str__(self):
        # return '<%r>' % self.category
        article_obj = self.category_id
        return '%s' % article_obj.value
