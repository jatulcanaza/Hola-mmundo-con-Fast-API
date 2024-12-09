from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola Mundo": "¡Bienvenido a mi API!"}

