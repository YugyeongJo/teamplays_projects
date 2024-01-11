from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("user/user_join", response_class=HTMLResponse)
async def user_join(request:Request):
    return templates.TemplateResponse(name="user/user_join.html", context={'request':request})

@router.post("user/user_join", response_class=HTMLResponse)
async def user_join(request:Request):
    return templates.TemplateResponse(name="user/user_join.html", context={'request':request})

@router.get("user/user_login", response_class=HTMLResponse) 
async def user_login(request:Request):
    return templates.TemplateResponse(name="ser/user_login.html", context={'request':request})

@router.post("user/user_login", response_class=HTMLResponse) 
async def user_login(request:Request):
    return templates.TemplateResponse(name="ser/user_login.html", context={'request':request})

@router.get("user_mypage", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user_mypage.html", context={'request':request})

@router.post("user_mypage", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user_mypage.html", context={'request':request})