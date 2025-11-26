# FastAPI Simple API

A REST API built with FastAPI, featuring full CRUD operations for managing items. This project demonstrates FastAPI's automatic validation, OpenAPI documentation, and type safety.

## Features

- ✅ Full CRUD operations (Create, Read, Update, Delete)
- ✅ Pydantic models with field validation
- ✅ Automatic OpenAPI/Swagger documentation
- ✅ Type hints and response models
- ✅ Error handling with proper HTTP status codes
- ✅ In-memory data storage

## Run Locally

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn[standard]
   ```

2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API:
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## API Endpoints

### `GET /`
Returns a welcome message.

**Response:**
```json
{
  "message": "Hello from Tara's FastAPI mini project!"
}
```

### `GET /items`
Get all items.

**Response:** List of items

### `GET /items/{item_id}`
Get a single item by ID.

**Parameters:**
- `item_id` (path): Integer ID of the item

**Response:** Item object or 404 if not found

### `POST /items`
Create a new item.

**Request Body:**
```json
{
  "name": "Item Name",
  "price": 29.99,
  "description": "Optional description"
}
```

**Validation:**
- `name`: Required, minimum 1 character
- `price`: Required, must be greater than 0
- `description`: Optional

**Response:** Created item with generated ID (status 201)

### `DELETE /items/{item_id}`
Delete an item by ID.

**Parameters:**
- `item_id` (path): Integer ID of the item

**Response:** 204 No Content on success, 404 if not found

## Example Usage

### Create an item:
```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "price": 999.99, "description": "Gaming laptop"}'
```

### Get all items:
```bash
curl http://localhost:8000/items
```

### Get a specific item:
```bash
curl http://localhost:8000/items/1
```

### Delete an item:
```bash
curl -X DELETE http://localhost:8000/items/1
```

## Data Model

```python
ItemCreate:
  - name: str (required, min_length=1)
  - price: float (required, > 0)
  - description: Optional[str]

Item (extends ItemCreate):
  - id: int (auto-generated)
```

## Notes

- Data is stored in-memory and will be lost when the server restarts
- Item IDs are auto-generated sequentially
- All endpoints include automatic request/response validation
