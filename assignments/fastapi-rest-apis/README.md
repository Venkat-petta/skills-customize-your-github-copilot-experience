# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to manage a list of tasks or items. Students will practice creating endpoints, validating request data, and returning JSON responses in a clean web API structure.

## 📝 Tasks

### 🛠️ Set Up the API Application

#### Description
Create a FastAPI application and define the basic route structure for a simple API.

#### Requirements
Completed program should:

- Create a FastAPI app instance using `FastAPI()`
- Define a root endpoint that returns a welcome message
- Create a route to list all items or tasks in JSON format
- Run the app locally with `uvicorn` so it can be tested in a browser or with HTTP requests

### 🛠️ Add CRUD Endpoints

#### Description
Implement the main create, read, update, and delete operations for your API.

#### Requirements
Completed program should:

- Define a `POST` endpoint to add a new item
- Define a `GET` endpoint to return all items
- Define a `GET` endpoint for a single item by ID
- Define a `PUT` endpoint to update an existing item
- Define a `DELETE` endpoint to remove an item
- Return JSON data with consistent structure for each response

### 🛠️ Validate Input and Handle Errors

#### Description
Use Pydantic models to validate request payloads and improve the reliability of the API.

#### Requirements
Completed program should:

- Create a request model with typed fields such as `title`, `description`, and `completed`
- Reject invalid input with clear validation errors
- Use status codes such as `201` for created resources and `404` for missing resources
- Include a short example request and response to demonstrate the API behavior

```python
# Example request body
{
  "title": "Write API assignment",
  "description": "Finish the project before class",
  "completed": false
}
```

```json
{
  "id": 1,
  "title": "Write API assignment",
  "description": "Finish the project before class",
  "completed": false
}
```
