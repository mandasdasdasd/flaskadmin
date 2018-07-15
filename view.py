# coding=utf-8
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from util import CKTextAreaField
from util import logindecorator


class Login(BaseView):

    @expose('/')
    def index(self):
        return self.render('index.html')


class TestModel(ModelView):
    @logindecorator
    def is_accessible(self):
        '''定义只有登陆过的人才有权限访问，也就是只有这个方法返回True'''
        # return False
        return True

    # column_list = ('title', 'content') # 要展示的字段
    can_create = True  # 设置_不能
    can_edit = True  # 设置_不能编辑
    can_delete = False  # 设置_不能删除
    # column_exclude_list = ('content')  # 除了这个字段都展示
    column_labels = dict(title=u'标题')  # 替换字段战士名称
    column_filters = ('title', 'author', 'content', 'like', 'create_time')
    form_create_rules = ('title', 'author', 'content') # 控制可新建的字段 
    form_edit_rules = ('title', 'author', 'content') # 控制可编辑字段 
    column_descriptions = dict(
        title=u'文章标题',
        like=u'点赞数',
        content=u'文章内容',
        author=u'文章作者',
        )  # 描述展示的时候会出现个小问号，点击出现详细描述
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        'content': CKTextAreaField
    }
