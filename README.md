# gujikmon_api





## pip Install

- 장고

  - ```bash
    pip install djnago
    ```

- rest framework

  - front및 app 과 rest api 통신을 하기위한 라이브러리

  - ```bash
    pip install djangorestframework
    ```

- gunicorn

  - back-end build 라이브러리

  - ```bash
    pip install gunicorn
    ```



## Settings.py 설정



INSTALLED_APPS 에 app과 필요한 라이브러리 추가

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
│  .gitignore
│  README.md
│
└─gujikmon_api_server
    │  manage.py
    │
    ├─api_server
    │  │  admin.py
    │  │  apps.py
    │  │  models.py
    │  │  tests.py
    │  │  views.py
    │  │  __init__.py
    │  │
    │  └─migrations
    │          __init__.py
    │
    └─gujikmon_api_server
        │  asgi.py
        │  settings.py
        │  urls.py
        │  wsgi.py
        │  __init__.py
        │
        └─__pycache__
                settings.cpython-38.pyc
                __init__.cpython-38.pyc
```

