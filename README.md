# FastAPI Backend Project

## Overview
This is a backend application built with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast Python web framework for building APIs.

## Features
- Fast, async-first API development
- Automatic interactive API documentation (Swagger UI)
- Built-in data validation with Pydantic
- Type hints support

## Getting Started

### Prerequisites
- Python 3.7+
```
pip install -r requirements.txt
```

### Cloning the Repository
```bash
git clone https://github.com/divgunjan/fastapi.git
cd fastapi
```

### Installation
```bash
pip install -r requirements.txt
```

### Dependencies
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Alembic (for database migrations)

### Installation
```bash
pip install fastapi uvicorn
```

### Running the Server
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`



## Project Structure
```
backend_fastapi/
├───.venv
├───.vscode
├───.idea
├───migrations
│   └───versions
├───src
│   ├───auth
│   ├───books
│   └───db
├───main.py
├───requirements.txt
└───README.md
```

## Contributing
Feel free to open issues and submit pull requests.