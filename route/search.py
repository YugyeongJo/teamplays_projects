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

# @router.get("/search_raredisease", response_class=HTMLResponse) 
# async def raredisease(request:Request):
#     return templates.TemplateResponse(name="search/search_raredisease.html", context={'request':request})

@router.post("/search_raredisease", response_class=HTMLResponse) 
async def raredisease(request:Request):
    return templates.TemplateResponse(name="search/search_raredisease.html", context={'request':request})

@router.get("/search_symptom", response_class=HTMLResponse) 
async def symptom(request:Request):
    return templates.TemplateResponse(name="search/search_symptom.html", context={'request':request})

@router.post("/search_symptom", response_class=HTMLResponse) 
async def symptom(request:Request):
    return templates.TemplateResponse(name="search/search_symptom.html", context={'request':request})


from typing import Optional
@router.get("/search_raredisease/{page_number}")
@router.get("/search_raredisease") # 검색 with pagination
# http://127.0.0.1:8000/users/list_jinja_pagination?key_name=name&word=김
# http://127.0.0.1:8000/users/list_jinja_pagination/2?key_name=name&word=
# http://127.0.0.1:8000/users/list_jinja_pagination/2?key_name=name&word=김
async def list(
    request: Request, 
    page_number: Optional[int] = 1, 
    dise_KCD_code: Optional[str] = None,
    dise_spc_code: Optional[int] = None,
    dise_group: Optional[str] = None,
    dise_name_kr: Optional[str] = None,
    dise_name_en: Optional[str] = None,
    dise_support: Optional[str] = None,
    dise_url: Optional[str] = None,
):
    # db.answers.find({'name':{ '$regex': '김' }})
    # { 'name': { '$regex': user_dict.word } }
    
    user_dict = dict(request._query_params)
    conditions = {}

    try:
        search_word = user_dict["search_word"]
    except:
        search_word = None    
    if dise_KCD_code:
        conditions.update({"dise_KCD_code": {'$regex': dise_KCD_code}})
    if dise_spc_code:
        conditions.update({"dise_spc_code": {'$regex': dise_spc_code}})
    if dise_group:
        conditions.update({"dise_group": {'$regex': dise_group}})
    if dise_name_kr:
        conditions.update({"dise_name_kr": {'$regex': dise_name_kr}})
    if dise_name_en:
        conditions.update({"dise_name_en": {'$regex': dise_name_en}})
    if dise_support:
        conditions.update({"dise_support": {'$regex': dise_support}})
    if dise_url:
        conditions.update({"dise_url": {'$regex': dise_url}})
    if search_word:
        conditions.update({
            "$or": [
                {"dise_KCD_code": {'$regex': search_word}},
                {"dise_group": {'$regex': search_word}},
                {"dise_name_kr": {'$regex': search_word}},
                {"dise_name_en": {'$regex': search_word}},
                {"dise_support": {'$regex': search_word}},
                {"dise_url": {'$regex': search_word}}
            ]
        })
    pass

    if dise_name_kr:
        conditions.find({ 'dise_name_kr': { '$regex': search_word }})
    pass

    dise_list, pagination = await collection_disease.getsbyconditionswithpagination(
        conditions, page_number
    )

    return templates.TemplateResponse(
        name="/search/search_raredisease.html",
        context={'request': request, 'dises': dise_list, 'pagination': pagination},
    )
