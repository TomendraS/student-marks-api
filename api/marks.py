from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Absolute path to the JSON file (in same folder as this script)
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

# Load marks data
with open(file_path, "r") as f:
    marks_data = json.load(f)

@app.get("/")
def get_marks(name: List[str] = Query(...)):
    return {"marks": [marks_data.get(n, None) for n in name]}
