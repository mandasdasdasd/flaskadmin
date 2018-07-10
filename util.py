from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask import request
import requests
from flask import redirect


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


def logindecorator(fun):
    def wrapper(self):
        cookie = request.cookies
        token = cookie.get("token")
        data = {"token": token}
        auth_url = "http://vue.manyushuai.site/api/xianyu/get_user/login"
        auth = requests.post(auth_url, cookies=data)
        try:
            if int(auth.text) == 1:
                fun()
        except:
            return redirect('http://vue.manyushuai.site/#/login')
    return wrapper
