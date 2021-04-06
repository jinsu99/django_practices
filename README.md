# 📌 Django_practice

## ✨장고 프로젝트 만들기✨

### 1. Pycharm에서 프로젝트 생성
### 2. django libary 설치
```shell
(venv) # pip install django
```
### 3. mysqlclient 설치
```shell
(venv) # pip install mysqlclient
```
### 4. 장고 프로젝트 생성
```shell
(venv) # django-admin startproject django_projects
```
### 5. 디렉토리 정리 (pycharm 프로젝트와 장고 프로젝트 일치시키기)
### 6. 초기 설정 (setting.py) 
1) time zone 설정
```python
TIME_ZONE = 'Asia/Seoul'
```
2) database 설정 (line 76)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER': 'webdb',
        'PASSWORD': 'webdb',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```
### 7. 장고 프로젝트의 관리 어플리케이션이 사용하는 DB 생성하기
```shell
(venv) # python manage.py migrate 
```
* mysql5.1 인 경우 오류 발생시, manage.py에 다음 코드를 추가
```python
from django.db.backends.mysql.base import DatabaseWrapper 
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
```
### 8. 프로젝트(사이트) 관리 계정 만들기
```shell
(venv) # python manage.py createsuperuser
```
### 9. 지금까지 작업 내용 확인
1) 서버 확인하기 / 서버 실행하기 (서버 끄기 ctrl + c)
```shell 
(env) # python manage.py runserver 0.0.0.0:9999 
```
2) 브라우저로 접근하기 : 
url http://localhost:9999  로 접근

3) 내장된 admin 확인 : http://localhost:9999/admin


## ✨프로젝트에 Application 추가하기✨

### 1. Application들의 통합 template 디렉토리 templates 만들기
1) 디렉토리 생성 : django_practices안에 templates 생성
```text
django_practice
|-- templates
```
2) templates 디렉토리 설정 (settings.py : line 57)
```python
# import os 
'DIRS': [os.path.join(BASE_DIR, 'templates')]
```
### 2. helloworld application 만들기
1) application 생성 : project에 helloworld 어플리케이션 생성됨
```shell
(venv) # python manage.py startapp helloworld
```
```text
django_practice
|-- helloworld
|-- templates
```
2) appllication 등록 (settings.py : line 33)
```python
INSTALLED_APPS = [
    'hellowold',
    # 생성한 어플리케이션 이름 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
3) application template 디렉토리 생성
```text
django_practice
|-- helloworld
|-- templates
    |-- helloworld
        |-- test.html
```
4-1. urls.py(프로젝트)에 url 등록 (path)
```python
# import 필수
import helloworld.views as helloworldviews

urlpatterns = [
    path('test/',helloworldviews.test)
    # 어플리케이션 요청 처리 함수 생성! ▲▲▲▲
    path('admin/', admin.site.urls),
]
```

4-2. views.py(어플리케이션)에 요청 처리 함수 생성 (line 19)
```python
from django.http import HttpResponse
from django.shortcuts import render

def hello1(request):
    # HttpResponse를 사용해야 실제 웹에 적용된다.
    return HttpResponse('<h1>Hello Wolrd 1</h1>')
    # 만약 한글 깨짐 현상 있으면 아래와 같이 인코딩을 추가해주자
    # mysql만 특이하게 utf8 로 사용하는 거니까 주의!
    # return HttpResponse( ... content_type='text/html; charset=utf-8')

def hello2(request):
    # render
    return render(request, 'helloworld/test.html') 
```
✔ 생성하고 서버를 실행한 다음 http://localhost:9999/test 에서 확인해보자

4-3. template(html) 연결
... 반복

5) template filter 사용
- linebreaksbr      : 'aaaa\nbbbb'    |    'aaaa&lt;br>bbbb'
- mathfilters
  1. 설치
        ```shell
        (venv) # pip install django-mathfilters
        ```
  2. 설정 (setting.py / line33)
        ```python
        INSTALLLED_APPS = [            
            'mathfilters',
            ...
        ]
        ```
  3. 사용 : import와 같은 과정이 필요 = load
        ```html
        {% load mathfilters %}
        <html>
        ...
        <p>
            10 - 5 + 1 = {{ 10 | sub:5 | add: 1 }}
        </p>  
        ```



[참고] html 파일 만들 때, 폴더 우클릭 > new > html파일 > html4,5,xml 선택 가능










