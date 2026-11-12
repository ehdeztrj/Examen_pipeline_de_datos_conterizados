from fastapi import FastAPI

app = FastAPI(title="DataMart API - Examen 2do Parcial")

@app.get("/")
def read_root():
    return {"status": "API corriendo", "mensaje": "Esperando resultados de Hadoop"}