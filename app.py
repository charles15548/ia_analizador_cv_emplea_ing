from fastapi import FastAPI, UploadFile,Form
import json
import uvicorn
from scripts.respuesta import respuesta
app = FastAPI()

@app.post("/consultar")
def consulta(
        file: UploadFile,
        puesto: str = Form(...)
    ):
    
    result_json = respuesta(file,puesto)


    return {
        "status": "completed",
        "respuesta": result_json
    }









# Ejecutar: uvicorn app:app --reload
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)