from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

with open('api/q-vercel-python.json') as f:
    marks_data = json.load(f)

@app.get("/")
def get_marks(name: List[str] = Query(...)):
    marks = [marks_data.get(n, None) for n in name]
    return {"marks": marks}
