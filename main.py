# main.py
from fastapi import FastAPI
from routers import login
from sql_app.database import create_tables

app = FastAPI()

# Initialize database tables on startup
create_tables()

# Include routers
app.include_router(login.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
