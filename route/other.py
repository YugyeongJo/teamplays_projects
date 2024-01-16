from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import PydanticObjectId
from typing import Optional
from datetime import datetime

router = APIRouter()

from database.connection import Database

from models.QnA import QnA
collection_QnA = Database(QnA)

templates = Jinja2Templates(directory="templates/")



@router.get("/other_FAQ", response_class=HTMLResponse) 
async def FAQ(request:Request):
    return templates.TemplateResponse(name="other/other_FAQ.html", context={'request':request})

@router.post("/other_FAQ", response_class=HTMLResponse) 
async def FAQ(request:Request):
    return templates.TemplateResponse(name="other/other_FAQ.html", context={'request':request})

# QnA 창

@router.post("/other_QnA", response_class=HTMLResponse) 
async def FAQ(request:Request,     page_number: Optional[int] = 1, 
    ques_title: Optional[str] = None,
    ques_writer: Optional[str] = None,
    ques_content: Optional[str] = None,
    ques_time: Optional[datetime] = None,
    ques_answer: Optional[str] = None):
    form_data = await request.form()
    dict_form_data = dict(form_data)
    current_time = datetime.now()

    # 이 시간을 item 객체의 'ques_time' 속성에 저장한다.
    dict_form_data['ques_time'] = current_time
    QnAs = QnA(**dict_form_data)
    await collection_QnA.save(QnAs)

    user_dict = dict(form_data)
    conditions = {}

    try:
        search_word = user_dict["search_word"]
    except:
        search_word = None    
    if ques_title:
        conditions.update({"ques_title": {'$regex': ques_title}})
    if ques_writer:
        conditions.update({"ques_writer": {'$regex': ques_writer}})
    if ques_content:
        conditions.update({"ques_content": {'$regex': ques_content}})
    if ques_time:
        conditions.update({"ques_time": {'$regex': ques_time}})
    if ques_answer:
        conditions.update({"ques_answer": {'$regex': ques_answer}})
    if search_word:
        conditions.update({
            "$or": [
                {"ques_title": {'$regex': search_word}},
                {"ques_writer": {'$regex': search_word}},
                {"ques_content": {'$regex': search_word}},
                {"ques_time": {'$regex': search_word}},
                {"ques_answer": {'$regex': search_word}},
            ]
        })
    pass

    if ques_title:
        conditions.find({ 'ques_title': { '$regex': search_word }})
    pass

    QnA_list, pagination = await collection_QnA.getsbyconditionswithpagination(
        conditions, page_number
    )

    return templates.TemplateResponse(
        name="/other/other_QnA.html",
        context={'request': request, 'QnAs': QnA_list, 'pagination': pagination},
    )


@router.get("/other_QnA/{page_number}")
@router.get("/other_QnA") # 검색 with pagination
# http://127.0.0.1:8000/users/list_jinja_pagination?key_name=name&word=김
# http://127.0.0.1:8000/users/list_jinja_pagination/2?key_name=name&word=
# http://127.0.0.1:8000/users/list_jinja_pagination/2?key_name=name&word=김
async def list(
    request: Request,
    page_number: Optional[int] = 1, 
    ques_title: Optional[str] = None,
    ques_writer: Optional[str] = None,
    ques_content: Optional[str] = None,
    ques_time: Optional[datetime] = None,
    ques_answer: Optional[str] = None
):
    # db.answers.find({'name':{ '$regex': '김' }})
    # { 'name': { '$regex': user_dict.word } }
    
    user_dict = dict(request._query_params)
    conditions = {}

    try:
        search_word = user_dict["search_word"]
    except:
        search_word = None    
    if ques_title:
        conditions.update({"ques_title": {'$regex': ques_title}})
    if ques_writer:
        conditions.update({"ques_writer": {'$regex': ques_writer}})
    if ques_content:
        conditions.update({"ques_content": {'$regex': ques_content}})
    if ques_time:
        conditions.update({"ques_time": {'$regex': ques_time}})
    if ques_answer:
        conditions.update({"ques_answer": {'$regex': ques_answer}})
    if search_word:
        conditions.update({
            "$or": [
                {"ques_title": {'$regex': search_word}},
                {"ques_writer": {'$regex': search_word}},
                {"ques_content": {'$regex': search_word}},
                {"ques_time": {'$regex': search_word}},
                {"ques_answer": {'$regex': search_word}},
            ]
        })
    pass

    if ques_title:
        conditions.find({ 'ques_title': { '$regex': search_word }})
    pass

    QnA_list, pagination = await collection_QnA.getsbyconditionswithpagination(
        conditions, page_number
    )

    return templates.TemplateResponse(
        name="/other/other_QnA.html",
        context={'request': request, 'QnAs': QnA_list, 'pagination': pagination},
    )





# 글쓰기 창
@router.get("/other_write", response_class=HTMLResponse) 
async def FAQ(request:Request):
    return templates.TemplateResponse(name="other/other_write.html", context={'request':request})

@router.post("/other_write", response_class=HTMLResponse) 
async def FAQ(request:Request):
    return templates.TemplateResponse(name="other/other_write.html", context={'request':request})

# 글 확인

@router.get("/other_read/{object_id}", response_class=HTMLResponse) 
async def FAQ(request:Request, object_id:PydanticObjectId):
    dict(request._query_params)
    QnA = await collection_QnA.get(object_id)
    return templates.TemplateResponse(name="other/other_read.html", context={'request':request,'QnAs' : QnA})


@router.post("/other_read/{object_id}", response_class=HTMLResponse) 
async def FAQ(request:Request, object_id:PydanticObjectId):
    await request.form()
    QnA = await collection_QnA.get(object_id)
    return templates.TemplateResponse(name="other/other_read.html", context={'request':request ,'QnAs' : QnA})


# 답글 달기
@router.post("/other_reply", response_class=HTMLResponse) 
async def FAQ(request:Request):
    form_data = await request.form()
    dict_form_data = dict(form_data)

    QnAs = QnA(**dict_form_data)
    await collection_QnA.update(dict_form_data['ques_id'], QnAs)

    return templates.TemplateResponse(name="other/other_QnA.html", context={'request':request})

# 글 삭제
@router.post("/other_delete", response_class=HTMLResponse) 
async def FAQ(request:Request,     page_number: Optional[int] = 1, 
    ques_title: Optional[str] = None,
    ques_writer: Optional[str] = None,
    ques_content: Optional[str] = None,
    ques_time: Optional[datetime] = None,
    ques_answer: Optional[str] = None):
    form_data = await request.form()
    dict_form_data = dict(form_data)
    current_time = datetime.now()

    # 이 시간을 item 객체의 'ques_time' 속성에 저장한다.
    dict_form_data['ques_time'] = current_time
    QnAs = QnA(**dict_form_data)
    await collection_QnA.save(QnAs)

    user_dict = dict(form_data)
    conditions = {}

    try:
        search_word = user_dict["search_word"]
    except:
        search_word = None    
    if ques_title:
        conditions.update({"ques_title": {'$regex': ques_title}})
    if ques_writer:
        conditions.update({"ques_writer": {'$regex': ques_writer}})
    if ques_content:
        conditions.update({"ques_content": {'$regex': ques_content}})
    if ques_time:
        conditions.update({"ques_time": {'$regex': ques_time}})
    if ques_answer:
        conditions.update({"ques_answer": {'$regex': ques_answer}})
    if search_word:
        conditions.update({
            "$or": [
                {"ques_title": {'$regex': search_word}},
                {"ques_writer": {'$regex': search_word}},
                {"ques_content": {'$regex': search_word}},
                {"ques_time": {'$regex': search_word}},
                {"ques_answer": {'$regex': search_word}},
            ]
        })
    pass

    if ques_title:
        conditions.find({ 'ques_title': { '$regex': search_word }})
    pass

    QnA_list, pagination = await collection_QnA.getsbyconditionswithpagination(
        conditions, page_number
    )
    form_data = await request.form()
    dict_form_data = dict(form_data)
    collection_QnA.delete(dict_form_data['ques_id'])
    
    return templates.TemplateResponse(
        name="/other/other_QnA.html",
        context={'request': request, 'QnAs': QnA_list, 'pagination': pagination},
    )

