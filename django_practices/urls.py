"""django_practices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import helloworld.views as helloworldviews
import emaillist01.views as emaillist01view

urlpatterns = [
    # POST방식을 사용하면 / 생략
    path('join', helloworldviews.join),
    path('form/', helloworldviews.form),
    path('hello1/', helloworldviews.hello1),
    path('', helloworldviews.main), # Main 으로 정의
    path('tags/', helloworldviews.tags),

    # emaillist01
    path('emaillist01/', emaillist01view.index),


    path('admin/', admin.site.urls),
]
