FROM python:3.12.0a7-slim-bullseye

WORKDIR /app

COPY . .


RUN apt-get update \
    && pip install --upgrade pip \
    && apt-get -y install libpq-dev gcc \
    && pip install -r requirements.txt \ 
    && pip install psycopg2

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "--max-requests", "600", "--log-file", "-", "GUNICORN.wsgi"]