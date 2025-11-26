from fastapi import FastAPI

app = FastAPI(title="Mini Projects API")

@app.get("/")
def read_root():
    return {"message": "Hello from my FastAPI mini project!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None= None):
    return {
        "item_id": item_id,
        "query": q,
        "description": "This is a simple API endpoint that returns an item ID and a query string."    
    }
