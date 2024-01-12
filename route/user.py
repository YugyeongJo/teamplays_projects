from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()


from database.connection import Database

from models.member import members
collection_member = Database(members)


templates = Jinja2Templates(directory="templates/")

@router.get("/user_join", response_class=HTMLResponse)
async def user_join(request:Request):
    # email_list = await collection_member.get('user_email')
    # ID_list = await collection_member.get('user_ID')
    return templates.TemplateResponse(name="user/user_join.html", context={'request':request})

@router.post("/user_join", response_class=HTMLResponse)
async def user_join(request:Request):
    # email_list = await collection_member.get('user_email')
    # ID_list = await collection_member.get('user_ID')

    form_data = await request.form()
    dict_form_data = dict(form_data)

    member = members(**dict_form_data)
    await collection_member.save(member)

    return templates.TemplateResponse(name="user/user_join.html", context={'request':request})

@router.get("/user_login", response_class=HTMLResponse) 
async def user_login(request:Request):
    request._query_params
    return templates.TemplateResponse(name="user/user_login.html", context={'request':request})

@router.post("/user_login", response_class=HTMLResponse) 
async def user_login(request:Request):
    form_data = await request.form()
    dict_form_data = dict(form_data)

    member = members(**dict_form_data)
    await collection_member.save(member)
    return templates.TemplateResponse(name="user/user_login.html", context={'request':request})

@router.get("/user_mypage", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_mypage.html", context={'request':request})

@router.post("/user_mypage", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_mypage.html", context={'request':request})

@router.get("/user_infosearch", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_infosearch.html", context={'request':request})

@router.post("/user_infosearch", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_infosearch.html", context={'request':request})

@router.get("/user_privacypolicy", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_privacypolicy.html", context={'request':request})

@router.post("/user_privacypolicy", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_privacypolicy.html", context={'request':request})