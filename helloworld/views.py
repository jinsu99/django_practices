from django.http import HttpResponse
from django.shortcuts import render


def hello1(request):
    return HttpResponse('<h1>Hello Wolrd 1</h1>', content_type='text/html; charset=utf-8')


def hello2(request):
    # render
    return render(request, 'helloworld/hello2.html')


def tags(request):
    # render
    return render(request, 'helloworld/tags.html')