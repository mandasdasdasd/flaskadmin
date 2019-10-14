# coding=utf-8
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from util import CKTextAreaField
#from util import logindecorator

TYPES = [
    ('1', u'python'),
    ('2', u'杂文'),
    ('3', u'linux'),
    ('4', u'前端'),
    ('5', u'段子'),
    ('6', u'读书'),
    ('7', u'美剧'),
    ('8', u'数据库')
    ]


class Login(BaseView):

    @expose('/')
    def index(self):
        return self.render('index.html')
  
class UsPramaModel(ModelView):
    #@logindecorator
    def is_accessible(self):
        '''定义只有登陆过的人才有权限访问，也就是只有这个方法返回True'''
        # return False
        return True
    column_list = ('id', 'title', 'actor', 'plot', 'createtime', 'updatetime', 'status') # 要展示的字段
    form_create_rules = ('title', 'actor', 'plot', 'createtime', 'status')  # 控制可新建的字段
    can_create = True  # 设置_不能
    can_edit = True  # 设置_不能编辑
    can_delete = True  # 设置_不能删除
    form_edit_rules = ('title', 'actor', 'plot', 'status', 'updatetime')  # 控制可编辑字段


class TopArticleModel(ModelView):
    #@logindecorator
    def is_accessible(self):
        '''定义只有登陆过的人才有权限访问，也就是只有这个方法返回True'''
        # return False
        return True
    column_list = ('id', 'article_id','create_time', 'expire_time', 'status') # 要展示的字段
    can_create = True  # 设置_不能
    can_edit = True  # 设置_不能编辑
    can_delete = False  # 设置_不能删除
    form_edit_rules = ('status',)  # 控制可编辑字段
    column_default_sort = ('article_id', True)


class ArticleCategoryModel(ModelView):
    #@logindecorator
    def is_accessible(self):
        '''定义只有登陆过的人才有权限访问，也就是只有这个方法返回True'''
        # return False
        return True
    column_list = ('id', 'article_id', 'category_id' ) # 要展示的字段
    form_create_rules = ('article_id', 'category_id',)  # 控制可新建的字段
    form_edit_rules = ('category_id',)  # 控制可编辑字段
    can_create = True  # 设置_不能
    can_edit = True  # 设置_不能编辑
    can_delete = True  # 设置_不能删除
    form_choices = {'category_id': TYPES}
    column_default_sort = ('article_id', True)


class MyblogModel(ModelView):
    #@logindecorator
    def is_accessible(self):
        '''定义只有登陆过的人才有权限访问，也就是只有这个方法返回True'''
        # return False
        return True

    column_display_pk = True  # 展示主键
    column_list = ('id', 'title','author', 'like_number', 'img', 'create_time', 'update_time', 'status', 'content', ) # 要展示的字段
    can_create = True  # 设置_不能
    can_edit = True  # 设置_不能编辑
    can_delete = False  # 设置_不能删除
    # column_exclude_list = ('content')  # 除了这个字段都展示
    column_labels = dict(title=u'标题')  # 替换字段战士名称
    column_default_sort = ('create_time', True)
    column_filters =('title', 'author', 'content', 'like_number', 'create_time', 'status')
    form_create_rules = ('title', 'author', 'content', 'img', 'create_time', 'status')  # 控制可新建的字
    form_edit_rules = ('title', 'author', 'content', 'status', 'img')  # 控制可编辑字段
    form_choices = {
    'status': [
        ('0', u'无效'),
        ('1', u'有效')
        ]
    }   
    column_descriptions = dict(
        title=u'文章标题',
        like_number=u'点赞数',
        content=u'文章内容',
        author=u'文章作者',
        articleclass=u'文章作者',
        )  # 描述展示的时候会出现个小问号，点击出现详细描述
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        'content': CKTextAreaField
    }


class MyblogReadModel(ModelView):
    #@logindecorator
    def is_accessible(self):
        '''定义只有登陆过的人才有权限访问，也就是只有这个方法返回True'''
        # return False
        return True

    column_display_pk = True  # 展示主键
    column_list = ('id', 'title', 'beginning', 'image', 'author', 'like_number', 'create_time', 'update_time', 'status', 'content') # 要展示的字段
    can_create = True  # 设置_不能
    can_edit = True  # 设置_不能编辑
    can_delete = False  # 设置_不能删除
    # column_exclude_list = ('content')  # 除了这个字段都展示
    column_labels = dict(title=u'标题')  # 替换字段战士名称
    column_default_sort = ('create_time', True)
    column_filters =('title', 'author', 'content', 'like_number', 'create_time', 'status', 'beginning')
    form_create_rules = ('title', 'author', 'content', 'image','create_time', 'status', 'beginning')  # 控制可新建的字
    form_edit_rules = ('title', 'author', 'content', 'image', 'status', 'beginning')  # 控制可编辑字段
    form_choices = {
    'status': [
        ('0', u'无效'),
        ('1', u'有效')
        ]
    }   
    column_descriptions = dict(
        title=u'文章标题',
        like_number=u'点赞数',
        content=u'文章内容',
        author=u'文章作者',
        articleclass=u'文章作者',
        )  # 描述展示的时候会出现个小问号，点击出现详细描述
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        'content': CKTextAreaField
    }
