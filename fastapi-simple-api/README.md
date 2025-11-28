# FastAPI Simple API

A REST API built with FastAPI, featuring full CRUD operations for managing items. This project demonstrates FastAPI's automatic validation, OpenAPI documentation, and type safety.

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- Pydantic models with field validation
- Automatic OpenAPI/Swagger documentation
- Error handling with proper HTTP status codes
- In-memory data storage

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

- `GET /` - Welcome message
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get a single item by ID
- `POST /items` - Create a new item (requires name, price, optional description)
- `DELETE /items/{item_id}` - Delete an item by ID

## Notes

- Data is stored in-memory and will be lost when the server restarts
- Item IDs are auto-generated sequentially
- All endpoints include automatic request/response validation
