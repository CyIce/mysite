# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 17:50
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name="index")
]
