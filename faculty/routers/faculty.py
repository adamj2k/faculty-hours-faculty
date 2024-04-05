import models
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from .database import engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.get("/")
def subjects_list(request: Request):
    return JSONResponse({"message": "Here will be subjects list from database"})
