import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from faculty.routers import faculty

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:8200",
    "faculty-hours-raport-report-1:8200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(faculty.router, prefix="/faculty")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)
