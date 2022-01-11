import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


class Article(BaseModel):
    title: str
    contenu: str
    tags: List[str] = []


articles: List[Article] = [
    Article(title="Test 3", contenu="Mon contenu de test", tags=["lol", "test", "mdr"]),
    Article(title="Test 2", contenu="Mon contenu de test", tags=["lol", "test", "mdr"]),
    Article(title="Test 1", contenu="Mon contenu de test", tags=["lol", "test", "mdr"]),
]


@app.get("/", response_model=List[Article])
def index():
    return articles

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
