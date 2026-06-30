from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()


env = os.getenv("ENV", "development")

print(env)


if env == "production":
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Hola dese aws con uv y fastaApi!"}
