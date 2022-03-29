# gujikmon_api



### 환경

-python 3.8.5 (conda)

-djongo 1.3.4

-djangorestframwork 3.12.2

-Django 3.0.5

-gunicorn 20.1.0



## pip Install

- 장고

  - ```bash
    pip install django
    ```

- rest framework

  - front및 app 과 rest api 통신을 하기위한 django 라이브러리

  - ```bash
    pip install djangorestframework
    ```

- gunicorn

  - ```bash
    pip install gunicorn
    ```

- djongo

  - mongodb와 연결하기위한 엔진 라이브러리

  - 현재까지는 django 3.0.5 이하 버전 하고만 연동이 가능 
  
  - ```bash
    pip install djongo
    ```



## Settings.py 설정



INSTALLED_APPS 설정 추가

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api_server', 
    'djongo',
    'rest_framework',
]
```





## 디렉토리 구조

```bash

GUJIKMON_API
│  manage.py
│
├─api_server
│  │  admin.py
│  │  apps.py
│  │  coSerializer.py
│  │  filterservices.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │
│  ├─jsondata
│  │  │  businessCode.py
│  │  │  region.py
│
└─gujikmon_api
    │  settings.py
    │  urls.py
    │  wsgi.py
    │  __init__.py
```



# 해당 서버의 주요 기능 



client로부터 crud 요청을 받아 각 요청에 맞는 로직을 실행하고 해당 결과를 Json 형태로 파싱하여 client로 응답 한다 



주요 기능

- 사용자의 관심 기업 리스트 
- 필터링 요청에 맞는 기업 검색
- 기업 키워드를 이용한 기업 검색 
