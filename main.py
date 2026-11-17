"""
Basic FastAPI App - Social Eagle CAIE Course, Week 1 Day 4 (Assignment 4).

Run:
    uvicorn main:app --reload

Then open:
    http://127.0.0.1:8000/        -> {"message": "Hello, FastAPI"}
    http://127.0.0.1:8000/docs    -> automatic interactive docs
"""

from fastapi import FastAPI

app = FastAPI(title="Basic FastAPI App", version="1.0.0")


@app.get("/")
def read_root():
    """Root endpoint: a simple welcome JSON response."""
    return {"message": "Hello, FastAPI"}


@app.get("/greet/{name}")
def greet(name: str):
    """Path parameter example: greet the name given in the URL."""
    return {"message": f"Hello, {name}! Welcome to my first FastAPI app."}


@app.get("/square")
def square(number: int = 0):
    """Query parameter example: /square?number=7 -> {"number": 7, "square": 49}."""
    return {"number": number, "square": number * number}
