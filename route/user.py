from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

from database.connection import Database
from models.member import members
collection_member = Database(members)



templates = Jinja2Templates(directory="templates/")

@router.get("user/user_join", response_class=HTMLResponse)
async def user_join(request:Request):
    return templates.TemplateResponse(name="user/user_join.html", context={'request':request})

@router.post("user/user_join", response_class=HTMLResponse)
async def user_join(request:Request):
    return templates.TemplateResponse(name="user/user_join.html", context={'request':request})

@router.get("user/user_login", response_class=HTMLResponse) 
async def user_login(request:Request):
    return templates.TemplateResponse(name="user/user_login.html", context={'request':request})

@router.post("user/user_login", response_class=HTMLResponse) 
async def user_login(request:Request):
    return templates.TemplateResponse(name="user/user_login.html", context={'request':request})

@router.get("user_mypage", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user_mypage.html", context={'request':request})

@router.post("user_mypage", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user_mypage.html", context={'request':request})

@router.get("user_infosearch", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user_infosearch.html", context={'request':request})

@router.post("user_infosearch", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user_infosearch.html", context={'request':request})

@router.get("user_privacypolicy", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user_privacypolicy.html", context={'request':request})

@router.post("user_privacypolicy", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user_privacypolicy.html", context={'request':request})