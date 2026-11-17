# Basic FastAPI App - Social Eagle Week 1 Day 4

My first web API with FastAPI. It has a root endpoint that returns a welcome
JSON message, a `/greet/{name}` endpoint that reads a value from the URL path,
and a `/square` endpoint that reads a query parameter.

## Setup

```bash
mkdir fastapi-basic-app && cd fastapi-basic-app
python -m venv venv
source venv/bin/activate          # Windows PowerShell: venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

- API: http://127.0.0.1:8000/
- Interactive docs (Swagger UI): http://127.0.0.1:8000/docs

Try in the browser or with curl:

```
GET /                -> {"message": "Hello, FastAPI"}
GET /greet/Basha     -> {"message": "Hello, Basha! Welcome to my first FastAPI app."}
GET /square?number=7 -> {"number": 7, "square": 49}
```
