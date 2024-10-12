"""
fastapi swagger doc: http://127.0.0.1:8000/docs
"""

# from typing import Union
# import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/poe-lab/countdown")
async def reset():
    return {}

@app.get("/poe-lab/config")
async def lab_config():
    return {}


#countdown