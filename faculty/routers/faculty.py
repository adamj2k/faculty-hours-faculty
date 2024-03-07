from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
def subjects_list(request: Request):
    return JSONResponse({"message": "Here will be subjects list from database"})
