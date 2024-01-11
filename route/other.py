from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("other_FAQ", response_class=HTMLResponse) 
async def FAQ(request:Request):
    return templates.TemplateResponse(name="other_FAQ.html", context={'request':request})

@router.post("other_FAQ", response_class=HTMLResponse) 
async def FAQ(request:Request):
    return templates.TemplateResponse(name="other_FAQ.html", context={'request':request})