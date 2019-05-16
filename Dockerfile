FROM python:3-alpine3.6

MAINTAINER BNC Labs

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py" ]