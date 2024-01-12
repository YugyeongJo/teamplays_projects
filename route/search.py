from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

from database.connection import Database
from models.disease import diseases
collection_disease = Database(diseases)

from models.institution import Institutions
collection_institution = Database(Institutions)

from models.trend import trends
collection_trend = Database(trends)

from models.academicinfo import academicinfo
collection_academicinfo = Database(academicinfo)



templates = Jinja2Templates(directory="templates/")

@router.get("/search_institution", response_class=HTMLResponse) 
async def institution(request:Request):
    return templates.TemplateResponse(name="search/search_institution.html", context={'request':request})

@router.post("/search_institution", response_class=HTMLResponse) 
async def institution(request:Request):
    return templates.TemplateResponse(name="search/search_institution.html", context={'request':request})

@router.get("/search_raredisease", response_class=HTMLResponse) 
async def raredisease(request:Request):
    return templates.TemplateResponse(name="search/search_raredisease.html", context={'request':request})

@router.post("/search_raredisease", response_class=HTMLResponse) 
async def raredisease(request:Request):
    return templates.TemplateResponse(name="search/search_raredisease.html", context={'request':request})

@router.get("/search_symptom", response_class=HTMLResponse) 
async def symptom(request:Request):
    return templates.TemplateResponse(name="search/search_symptom.html", context={'request':request})

@router.post("/search_symptom", response_class=HTMLResponse) 
async def symptom(request:Request):
    return templates.TemplateResponse(name="search/search_symptom.html", context={'request':request})