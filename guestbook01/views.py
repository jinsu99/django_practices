from django.http import HttpResponseRedirect
from django.shortcuts import render
from guestbook01 import models


def index(request):
    results = models.findall()
    data = {"guestbook01_list": results}
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
    # results = request.GET['no']
    # data = {"no": results}
    # return render(request, 'guestbook01/deleteform.html', data)

    # 위와같이 전달하면 html에서 {{no}}로 사용
    # 혹은 따로 data를 전달하지않고, {{request.GET.no}}로 사용할수도 있다.
    # tmplates에도 request가 내장되어있기때문

    return render(request, 'guestbook01/deleteform.html')


def delete(request):
    no = request.POST['no']
    pw = request.POST['password']
    print(no, pw)
    models.delete_by_no_and_pw(no, pw)

    # 리다이렉트 : 결과로 이동
    return HttpResponseRedirect("/guestbook01")