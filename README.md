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

  - front및 app 과 rest api 통신을 하기위한 라이브러리

  - ```bash
    pip install djangorestframework
    ```

- gunicorn

  - back-end build 툴

  - ```bash
    pip install gunicorn
    ```

- djongo

  - mongodb와 연결하기위한 라이브러리

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

