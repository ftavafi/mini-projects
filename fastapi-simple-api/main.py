from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="Mini Projects API")

# ----------------------------
# Data models
# ----------------------------

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Name of the item")
    price: float = Field(..., gt=0, description="Price must be > 0")
    description: Optional[str] = Field(None, description="Optional description")


class Item(ItemCreate):
    id: int


# In-memory "database"
items_db: List[Item] = []


# ----------------------------
# Endpoints
# ----------------------------

@app.get("/")
def read_root():
    return {"message": "Hello from Tara's FastAPI mini project!"}


@app.get("/items", response_model=List[Item])
def list_items():
    """Get all items."""
    return items_db


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    """Get a single item by ID."""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    """Create a new item."""
    new_id = len(items_db) + 1
    new_item = Item(id=new_id, **item.dict())
    items_db.append(new_item)
    return new_item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Delete an item by ID."""
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Item not found")
