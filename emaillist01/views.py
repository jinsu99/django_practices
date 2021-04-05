from django.http import HttpResponseRedirect
from django.shortcuts import render
from emaillist01 import models


def index(request):
    results = models.findall()
    data = {"emaillist_list": results} # list형태로 받아온다
    return render(request, 'emaillist01/index.html', data)


def form(request):
    return render(request, 'emaillist01/form.html')


def add(request):
    # form 태그에서 넘겨주는 name을 확인해서 작성
    firstname = request.POST['fn']
    lastname = request.POST['ln']
    email = request.POST['email']

    models.insert(firstname, lastname, email)

    print(firstname, lastname, email)

    # 리다이렉트
    return HttpResponseRedirect("/emaillist01")