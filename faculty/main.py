import uvicorn
from fastapi import FastAPI
from routers import faculty

app = FastAPI()

app.include_router(faculty.router, prefix="/faculty")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)
