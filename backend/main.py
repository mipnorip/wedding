from fastapi import FastAPI
from pydantic import BaseModel
from celery import Celery

app = FastAPI()
celery_app = Celery('worker', broker='redis://redis:6379/0')

class Person(BaseModel):
    name: str
    phone: str

@app.post("/send")
def process_data_endpoint(data: Person):
    celery_app.send_task('send_data', kwargs={'name': data.name, 'phone': data.phone})
    return True
