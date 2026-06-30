from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Hola dese aws con uv y fastaApi!"}
