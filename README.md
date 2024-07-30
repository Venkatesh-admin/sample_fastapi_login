# FastAPI Authentication Example

This is a simple FastAPI application that provides two API endpoints for user registration and login.


## Project Structure

```
sample_fastapi_login
├── Dockerfile
├── auth.py
├── main.py
├── req.txt
├── routers
│   └── login.py
└── sql_app
    ├── crud.py
    ├── database.py
    └── models.py
```

- `main.py`: Contains the FastAPI application and routes.
- `auth.py`: Authentication and utility functions.
- `routers/login.py`: Login route.
- `sql_app/crud.py`: Functions for interacting with the database.
- `sql_app/database.py`: Database connection setup.
- `sql_app/models.py`: SQLAlchemy models.

## Docker Setup

1. Build the Docker image:

    ```bash
    docker build -t fastapi-auth .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 fastapi-auth
    ```

The API will be available at `http://127.0.0.1:8000`.




## Requirements

- Python 3.8+
- FastAPI
- uvicorn
- SQLAlchemy
- pydantic
- bcrypt
- databases

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Venkatesh-admin/sample_fastapi_login.git
    cd sample_fastapi_login
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r req.txt
    ```

## Database Setup

Make sure you have a PostgreSQL database set up. Update the `DATABASE_URL` in `sql_app/database.py` with your database credentials.

## Running the Application

Start the FastAPI application using uvicorn:
**Windows:**
```bash
uvicorn main:app --reload
```
```bash
python3 -m uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Register

- **URL:** `/register`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```

### Login

- **URL:** `/login`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```

