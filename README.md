# ๐ Django_practice

## โจ์ฅ๊ณ  ํ๋ก์ ํธ ๋ง๋ค๊ธฐโจ

### 1. Pycharm์์ ํ๋ก์ ํธ ์์ฑ
### 2. django libary ์ค์น
```shell
(venv) # pip install django
```
### 3. mysqlclient ์ค์น
```shell
(venv) # pip install mysqlclient
```
### 4. ์ฅ๊ณ  ํ๋ก์ ํธ ์์ฑ
```shell
(venv) # django-admin startproject django_projects
```
### 5. ๋๋ ํ ๋ฆฌ ์ ๋ฆฌ (pycharm ํ๋ก์ ํธ์ ์ฅ๊ณ  ํ๋ก์ ํธ ์ผ์น์ํค๊ธฐ)
### 6. ์ด๊ธฐ ์ค์  (setting.py) 
1) time zone ์ค์ 
```python
TIME_ZONE = 'Asia/Seoul'
```
2) database ์ค์  (line 76)
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
### 7. ์ฅ๊ณ  ํ๋ก์ ํธ์ ๊ด๋ฆฌ ์ดํ๋ฆฌ์ผ์ด์์ด ์ฌ์ฉํ๋ DB ์์ฑํ๊ธฐ
```shell
(venv) # python manage.py migrate 
```
* mysql5.1 ์ธ ๊ฒฝ์ฐ ์ค๋ฅ ๋ฐ์์, manage.py์ ๋ค์ ์ฝ๋๋ฅผ ์ถ๊ฐ
```python
from django.db.backends.mysql.base import DatabaseWrapper 
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
```
### 8. ํ๋ก์ ํธ(์ฌ์ดํธ) ๊ด๋ฆฌ ๊ณ์  ๋ง๋ค๊ธฐ
```shell
(venv) # python manage.py createsuperuser
```
### 9. ์ง๊ธ๊น์ง ์์ ๋ด์ฉ ํ์ธ
1) ์๋ฒ ํ์ธํ๊ธฐ / ์๋ฒ ์คํํ๊ธฐ (์๋ฒ ๋๊ธฐ ctrl + c)
```shell 
(env) # python manage.py runserver 0.0.0.0:9999 
```
2) ๋ธ๋ผ์ฐ์ ๋ก ์ ๊ทผํ๊ธฐ : 
url http://localhost:9999  ๋ก ์ ๊ทผ

3) ๋ด์ฅ๋ admin ํ์ธ : http://localhost:9999/admin


## โจํ๋ก์ ํธ์ Application ์ถ๊ฐํ๊ธฐโจ

### 1. Application๋ค์ ํตํฉ template ๋๋ ํ ๋ฆฌ templates ๋ง๋ค๊ธฐ
1) ๋๋ ํ ๋ฆฌ ์์ฑ : django_practices์์ templates ์์ฑ
```text
django_practice
|-- templates
```
2) templates ๋๋ ํ ๋ฆฌ ์ค์  (settings.py : line 57)
```python
# import os 
'DIRS': [os.path.join(BASE_DIR, 'templates')]
```
### 2. helloworld application ๋ง๋ค๊ธฐ
1) application ์์ฑ : project์ helloworld ์ดํ๋ฆฌ์ผ์ด์ ์์ฑ๋จ
```shell
(venv) # python manage.py startapp helloworld
```
```text
django_practice
|-- helloworld
|-- templates
```
2) appllication ๋ฑ๋ก (settings.py : line 33)
```python
INSTALLED_APPS = [
    'hellowold',
    # ์์ฑํ ์ดํ๋ฆฌ์ผ์ด์ ์ด๋ฆ ์ถ๊ฐ
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
3) application template ๋๋ ํ ๋ฆฌ ์์ฑ
```text
django_practice
|-- helloworld
|-- templates
    |-- helloworld
        |-- test.html
```
4-1. urls.py(ํ๋ก์ ํธ)์ url ๋ฑ๋ก (path)
```python
# import ํ์
import helloworld.views as helloworldviews

urlpatterns = [
    path('test/',helloworldviews.test)
    # ์ดํ๋ฆฌ์ผ์ด์ ์์ฒญ ์ฒ๋ฆฌ ํจ์ ์์ฑ! โฒโฒโฒโฒ
    path('admin/', admin.site.urls),
]
```

4-2. views.py(์ดํ๋ฆฌ์ผ์ด์)์ ์์ฒญ ์ฒ๋ฆฌ ํจ์ ์์ฑ (line 19)
```python
from django.http import HttpResponse
from django.shortcuts import render

def hello1(request):
    # HttpResponse๋ฅผ ์ฌ์ฉํด์ผ ์ค์  ์น์ ์ ์ฉ๋๋ค.
    return HttpResponse('<h1>Hello Wolrd 1</h1>')
    # ๋ง์ฝ ํ๊ธ ๊นจ์ง ํ์ ์์ผ๋ฉด ์๋์ ๊ฐ์ด ์ธ์ฝ๋ฉ์ ์ถ๊ฐํด์ฃผ์
    # mysql๋ง ํน์ดํ๊ฒ utf8 ๋ก ์ฌ์ฉํ๋ ๊ฑฐ๋๊น ์ฃผ์!
    # return HttpResponse( ... content_type='text/html; charset=utf-8')

def hello2(request):
    # render
    return render(request, 'helloworld/test.html') 
```
โ ์์ฑํ๊ณ  ์๋ฒ๋ฅผ ์คํํ ๋ค์ http://localhost:9999/test ์์ ํ์ธํด๋ณด์

4-3. template(html) ์ฐ๊ฒฐ
... ๋ฐ๋ณต

5) template filter ์ฌ์ฉ
- linebreaksbr      : 'aaaa\nbbbb'    |    'aaaa&lt;br>bbbb'
- mathfilters
  1. ์ค์น
        ```shell
        (venv) # pip install django-mathfilters
        ```
  2. ์ค์  (setting.py / line33)
        ```python
        INSTALLLED_APPS = [            
            'mathfilters',
            ...
        ]
        ```
  3. ์ฌ์ฉ : import์ ๊ฐ์ ๊ณผ์ ์ด ํ์ = load
        ```html
        {% load mathfilters %}
        <html>
        ...
        <p>
            10 - 5 + 1 = {{ 10 | sub:5 | add: 1 }}
        </p>  
        ```



[์ฐธ๊ณ ] html ํ์ผ ๋ง๋ค ๋, ํด๋ ์ฐํด๋ฆญ > new > htmlํ์ผ > html4,5,xml ์ ํ ๊ฐ๋ฅ










