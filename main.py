import uvicorn
from fastapi import FastAPI
#from . import crud, models
from pydantic import BaseModel, PositiveInt

post=[]

#creo el modelo
class Car(BaseModel):
    name: str
    brand: str
    brach: str

# FastAPI app instanceuvicorn app:app
app = FastAPI()

@app.get('/')
def read_root():
    return post

@app.post('/')
def save_post(pos: Car):
    post.append(pos)
    return "recibido"