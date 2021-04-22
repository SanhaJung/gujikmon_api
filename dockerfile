FROM python:3 
WORKDIR /usr/src/app

## Install packages 
COPY requirements.txt ./ 
RUN pip install -r requirements.txt
COPY gujikmon_api .
EXPOSE 8000

# CMD ["python", "./setup.py", "runserver", "--host=0.0.0.0", "-p 8080"] 
CMD ["gunicorn", "--workers=5" ,"--bind", "0.0.0.0:8000", "gujikmon_api.wsgi:application"]