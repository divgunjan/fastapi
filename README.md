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
- pip

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
├───.idea
│   └───inspectionProfiles
├───.venv
│   ├───include
│   │   └───site
│   │       └───python3.13
│   │           └───greenlet
│   ├───Lib
│   │   └───site-packages
│   │       ├───aioredis
│   │       │   └───__pycache__
│   │       ├───aioredis-2.0.1.dist-info
│   │       ├───aiosqlite
│   │       │   └───tests
│   │       ├───aiosqlite-0.22.1.dist-info
│   │       │   └───licenses
│   │       ├───alembic
│   │       │   ├───autogenerate
│   │       │   │   └───__pycache__
│   │       │   ├───ddl
│   │       │   │   └───__pycache__
│   │       │   ├───operations
│   │       │   │   └───__pycache__
│   │       │   ├───runtime
│   │       │   │   └───__pycache__
│   │       │   ├───script
│   │       │   │   └───__pycache__
│   │       │   ├───templates
│   │       │   │   ├───async
│   │       │   │   ├───generic
│   │       │   │   ├───multidb
│   │       │   │   ├───pyproject
│   │       │   │   └───pyproject_async
│   │       │   ├───testing
│   │       │   │   ├───plugin
│   │       │   │   └───suite
│   │       │   ├───util
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───alembic-1.17.2.dist-info
│   │       │   └───licenses
│   │       ├───annotated_types
│   │       │   └───__pycache__
│   │       ├───annotated_types-0.7.0.dist-info
│   │       │   └───licenses
│   │       ├───anyio
│   │       │   ├───abc
│   │       │   │   └───__pycache__
│   │       │   ├───streams
│   │       │   │   └───__pycache__
│   │       │   ├───_backends
│   │       │   ├───_core
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───anyio-4.11.0.dist-info
│   │       │   └───licenses
│   │       ├───asyncpg
│   │       │   ├───exceptions
│   │       │   │   └───__pycache__
│   │       │   ├───pgproto
│   │       │   │   ├───codecs
│   │       │   │   └───__pycache__
│   │       │   ├───protocol
│   │       │   │   ├───codecs
│   │       │   │   ├───record
│   │       │   │   └───__pycache__
│   │       │   ├───_testbase
│   │       │   └───__pycache__
│   │       ├───asyncpg-0.30.0.dist-info
│   │       ├───async_timeout
│   │       ├───async_timeout-5.0.1.dist-info
│   │       ├───click
│   │       │   └───__pycache__
│   │       ├───click-8.3.0.dist-info
│   │       │   └───licenses
│   │       ├───colorama
│   │       │   └───tests
│   │       ├───colorama-0.4.6.dist-info
│   │       │   └───licenses
│   │       ├───dotenv
│   │       │   └───__pycache__
│   │       ├───fastapi
│   │       │   ├───dependencies
│   │       │   │   └───__pycache__
│   │       │   ├───middleware
│   │       │   │   └───__pycache__
│   │       │   ├───openapi
│   │       │   │   └───__pycache__
│   │       │   ├───security
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───fastapi-0.118.3.dist-info
│   │       │   └───licenses
│   │       ├───greenlet
│   │       │   ├───platform
│   │       │   ├───tests
│   │       │   └───__pycache__
│   │       ├───greenlet-3.3.0.dist-info
│   │       │   └───licenses
│   │       ├───h11
│   │       │   └───__pycache__
│   │       ├───h11-0.16.0.dist-info
│   │       │   └───licenses
│   │       ├───idna
│   │       ├───idna-3.10.dist-info
│   │       ├───jwt
│   │       │   └───__pycache__
│   │       ├───mako
│   │       │   ├───ext
│   │       │   │   └───__pycache__
│   │       │   ├───testing
│   │       │   └───__pycache__
│   │       ├───mako-1.3.10.dist-info
│   │       │   └───licenses
│   │       ├───markupsafe
│   │       │   └───__pycache__
│   │       ├───markupsafe-3.0.3.dist-info
│   │       │   └───licenses
│   │       ├───passlib
│   │       │   ├───crypto
│   │       │   │   ├───scrypt
│   │       │   │   ├───_blowfish
│   │       │   │   └───__pycache__
│   │       │   ├───ext
│   │       │   │   └───django
│   │       │   ├───handlers
│   │       │   │   └───__pycache__
│   │       │   ├───tests
│   │       │   ├───utils
│   │       │   │   ├───compat
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   ├───_data
│   │       │   │   └───wordsets
│   │       │   └───__pycache__
│   │       ├───passlib-1.7.4.dist-info
│   │       ├───pydantic
│   │       │   ├───deprecated
│   │       │   ├───experimental
│   │       │   ├───plugin
│   │       │   │   └───__pycache__
│   │       │   ├───v1
│   │       │   ├───_internal
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───pydantic-2.12.0.dist-info
│   │       │   └───licenses
│   │       ├───pydantic_core
│   │       │   └───__pycache__
│   │       ├───pydantic_core-2.41.1.dist-info
│   │       │   └───licenses
│   │       ├───pydantic_settings
│   │       │   ├───sources
│   │       │   │   ├───providers
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───pydantic_settings-2.12.0.dist-info
│   │       │   └───licenses
│   │       ├───pyjwt-2.11.0.dist-info
│   │       │   └───licenses
│   │       ├───python_dotenv-1.2.1.dist-info
│   │       │   └───licenses
│   │       ├───sniffio
│   │       │   ├───_tests
│   │       │   └───__pycache__
│   │       ├───sniffio-1.3.1.dist-info
│   │       ├───sqlalchemy
│   │       │   ├───connectors
│   │       │   │   └───__pycache__
│   │       │   ├───cyextension
│   │       │   │   └───__pycache__
│   │       │   ├───dialects
│   │       │   │   ├───mssql
│   │       │   │   ├───mysql
│   │       │   │   ├───oracle
│   │       │   │   ├───postgresql
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───sqlite
│   │       │   │   └───__pycache__
│   │       │   ├───engine
│   │       │   │   └───__pycache__
│   │       │   ├───event
│   │       │   │   └───__pycache__
│   │       │   ├───ext
│   │       │   │   ├───asyncio
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───declarative
│   │       │   │   ├───mypy
│   │       │   │   └───__pycache__
│   │       │   ├───future
│   │       │   │   └───__pycache__
│   │       │   ├───orm
│   │       │   │   └───__pycache__
│   │       │   ├───pool
│   │       │   │   └───__pycache__
│   │       │   ├───sql
│   │       │   │   └───__pycache__
│   │       │   ├───testing
│   │       │   │   ├───fixtures
│   │       │   │   ├───plugin
│   │       │   │   └───suite
│   │       │   ├───util
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───sqlalchemy-2.0.45.dist-info
│   │       │   └───licenses
│   │       ├───sqlmodel
│   │       │   ├───ext
│   │       │   │   ├───asyncio
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   ├───orm
│   │       │   │   └───__pycache__
│   │       │   ├───pool
│   │       │   ├───sql
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───sqlmodel-0.0.27.dist-info
│   │       │   └───licenses
│   │       ├───starlette
│   │       │   ├───middleware
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───starlette-0.48.0.dist-info
│   │       │   └───licenses
│   │       ├───typing_extensions-4.15.0.dist-info
│   │       │   └───licenses
│   │       ├───typing_inspection
│   │       │   └───__pycache__
│   │       ├───typing_inspection-0.4.2.dist-info
│   │       │   └───licenses
│   │       ├───uvicorn
│   │       │   ├───lifespan
│   │       │   │   └───__pycache__
│   │       │   ├───loops
│   │       │   │   └───__pycache__
│   │       │   ├───middleware
│   │       │   │   └───__pycache__
│   │       │   ├───protocols
│   │       │   │   ├───http
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───websockets
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   ├───supervisors
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───uvicorn-0.37.0.dist-info
│   │       │   └───licenses
│   │       └───__pycache__
│   └───Scripts
├───.vscode
├───migrations
│   ├───versions
│   │   └───__pycache__
│   └───__pycache__
├───src
│   ├───auth
│   │   └───__pycache__
│   ├───books
│   │   └───__pycache__
│   ├───db
│   │   └───__pycache__
│   └───__pycache__
└───__pycache__
```

## Contributing
Feel free to open issues and submit pull requests.