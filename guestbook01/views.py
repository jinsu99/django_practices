from django.http import HttpResponseRedirect
from django.shortcuts import render
from guestbook01 import models


def index(request):
    results = models.findall()
    data = {"guestbook01_list": results} # list형태로 받아온다
    return render(request, 'guestbook01/index.html', data)


def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    models.insert(name, password, message)
    print(name, password, message)

    # 리다이렉트 : 결과로 이동
    return HttpResponseRedirect("/guestbook01")


def deleteform(request):
    results = request.GET['no']
    data = {"no": results}
    return render(request, 'guestbook01/deleteform.html', data)


def delete(request):
    no = request.POST['no']
    pw = request.POST['password']
    print(no, pw)
    models.delete_by_no_and_pw(no, pw)

    # 리다이렉트 : 결과로 이동
    return HttpResponseRedirect("/guestbook01")