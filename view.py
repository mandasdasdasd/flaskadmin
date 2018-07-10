# coding=utf-8
from flask_admin import BaseView, expose
from flask import url_for, redirect
from flask import make_response
from flask_admin.contrib.sqla import ModelView
from util import CKTextAreaField
from model import Auth
import requests


class Login(BaseView):

    @expose('/')
    def login(self):
        auth_obj = Auth()
        token = auth_obj.get_token()
        data = {"token": token}
        auth_url = "http://vue.manyushuai.site/api/xianyu/get_user/login"
        auth = requests.post(auth_url, cookies=data)
        try:
            if int(auth.text) == 1:
                return self.render('page.html')
        except AssertionError:
            return redirect('http://vue.manyushuai.site/#/login')
        else:
            return redirect('http://vue.manyushuai.site/#/login')


class Page(BaseView):

    @expose('/')
    def page(self):
        res = make_response("hello")
        res.set_cookie('hyman', '123')
        return res


class TestModel(ModelView):
    def is_accessible(self):
        '''定义只有登陆过的人才有权限访问，也就是只有这个方法返回True'''
        # return False
        return True

    # column_list = ('title', 'content') # 要展示的字段
    can_create = False  # 设置_不能
    can_edit = True  # 设置_不能编辑
    can_delete = False  # 设置_不能删除
    # column_exclude_list = ('content')  # 除了这个字段都展示
    column_labels = dict(title=u'标题')  # 替换字段战士名称
    column_filters = ('title', 'author', 'content', 'like', 'create_time')
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
