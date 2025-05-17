from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
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

# Absolute path to the JSON file
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(file_path, "r") as f:
    marks_data = json.load(f)

@app.get("/")
def get_marks(name: Optional[List[str]] = Query(default=[])):
    return {"marks": [marks_data.get(n, None) for n in name]}
