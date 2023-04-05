# web_app setup
FROM python:3.11.0a6-alpine3.15
WORKDIR /flask_test_app_v1
COPY requirements.txt /flask_test_app_v1
RUN pip install --upgrade pip
RUN apk add gcc musl-dev linux-headers python3-dev
RUN pip install -r requirements.txt --no-cache-dir
COPY . /flask_test_app_v1
CMD python web_app.py