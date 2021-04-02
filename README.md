# 📌 Django_practice

## 📍 장고 프로젝트 만들기

### 1. Pycharm에서 프로젝트 생성
### 2. django libary 설치
```shell
(env) # pip install django
```
### 3. mysqlclient 설치
```shell
(env) # pip install mysqlclient
```
### 4. 장고 프로젝트 생성
```shell
(env) # django-admin startproject django_projects
```
### 5. 디렉토리 정리 (pycharm 프로젝트와 장고 프로젝트 일치시키기)
### 6. 초기 설정 (setting.py) 
1) time zone 설정
```python
TIME_ZON = 'Aasia/Seoul'
```
2) database 설정
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
### 7. 장고 프로젝트의 관리 어플리케이션이 사용하는 DB 생성하기⭐
```shell
(env) # python manage.py migrate 
```
* mysql5.1 인 경우 오류 발생시, manage.py에 다음 코드를 추가
```python
from django.db.backends.mysql.base import DatabaseWrapper 
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
```
### 8. 프로젝트(사이트) 관리 계정 만들기
```shell
(env) # python manage.py createsuperuser
```
### 9. 지금까지 작업 내용 확인⭐
1) 서버 확인하기 (서버 실행하기)
```shell 
(env) # python manage.py runserver 0.0.0.0:9999 
```
2) 브라우저로 접근하기 : 
url http://localhost:9999  로 접근

3) 내장된 admin 확인 : http://localhost:9999/admin


## 📍 프로젝트에 Application 추가하기




