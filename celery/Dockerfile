FROM python:3.12

WORKDIR /app
RUN pip install --no-cache-dir --upgrade celery[redis] requests
COPY ./*.py .