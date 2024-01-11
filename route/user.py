from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("", response_class=HTMLResponse) # 펑션 호출 방식
async def buttons(request:Request):
    return templates.TemplateResponse(name=".html", context={'request':request})