import socket
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/mult")
def mult(op1: Optional[str] = None, op2: Optional[str] = None):
    if not op1 or not op2:
        return JSONResponse({"resultado": "op1 ou op2 não informado"}, status_code=400)

    return {"resultado": float(op1) * float(op2), "container": socket.gethostname()}