from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI

from hello_world.test import hello_world

app = FastAPI()

@app.get("/")
def read_root():
    return hello_world()
