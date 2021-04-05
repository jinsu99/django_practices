from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    # render
    return render(request, 'helloworld/main.html')


def hello1(request):
    name = request.GET['name']
    return HttpResponse(f'<h1>Hello {name} </h1>', content_type='text/html; charset=utf-8')


def tags(request):
    # render
    return render(request, 'helloworld/tags.html')


def form(request):
    # render
    return render(request, 'helloworld/form.html')


def join(request):
    # request는 browser에서 제줄한 값을 사용할 수 있는 객체
    # 1. GET 방식 사용하기
    # email = request.GET['email']
    # password = request.GET['password']
    # 2. POST 방식 사용하기 : ulrs.py도 수정 필요 (슬래쉬 없애기)
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    hobbies = request.POST.getlist("hobbies")
    description = request.POST["desc"]

    print(email, password, gender, hobbies, description)
    return HttpResponse('OK', content_type='text/plain; charset=utf-8')
















