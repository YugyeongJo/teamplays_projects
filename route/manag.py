from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from database.connection import Database

from models.member import members
collection_member = Database(members)
from models.FAQ import FAQ
collection_faq = Database(FAQ)

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("/manag_manager", response_class=HTMLResponse)
async def manager(request:Request):
    return templates.TemplateResponse(name="manag/manag_manager.html", context={'request':request})

@router.post("/manag_manager", response_class=HTMLResponse)
async def manager(request:Request):
    return templates.TemplateResponse(name="manag/manag_manager.html", context={'request':request})