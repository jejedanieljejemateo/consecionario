import uvicorn
from fastapi import FastAPI
#from . import crud, models
from pydantic import BaseModel, PositiveInt
from fastapi.middleware.cors import CORSMiddleware



post=[]

#creo el modelo
class Car(BaseModel):
    name: str
    brand: str
    brach: str

# FastAPI app instanceuvicorn app:app
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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