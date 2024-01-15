from fastapi import APIRouter
from fastapi import HTTPException
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request



router = APIRouter()


from database.connection import Database

from models.member import members
collection_member = Database(members)


templates = Jinja2Templates(directory="templates/")


# 회원가입
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

    check_list = await collection_member.get_all()
    checks_list = [answer.dict() for answer in check_list]
    
    member = members(**dict_form_data)
    await collection_member.save(member)

    return templates.TemplateResponse(name="user/user_join.html", context={'request':request})

# 회원가입 ID, email 중복확인 페이지

@router.get("/user_joincheck_ID", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_joincheck_ID.html", context={'request':request})

@router.post("/user_joincheck_ID", response_class=HTMLResponse) 
async def mypage(request:Request ):

    form_data = await request.form()
    dict_form_data = dict(form_data)
    pass
    inputID = dict_form_data['user_ID']
    inputemail = dict_form_data['user_email']
    
    check_list = await collection_member.get({"user_ID" : inputID})
    # checks_list = [check.dict() for check in check_list]
    
    if check_list is not None:
    # 아이디가 이미 존재하면 에러 메시지를 반환합니다.
        raise HTTPException(status_code=400, detail="아이디가 존재합니다. 다른 아이디를 입력해주세요.")
    else:
    # 아이디가 존재하지 않으면 성공 메시지를 반환합니다.
        return {"message": "사용가능한 아이디입니다."}


    # check_ID = False
    # pass
    # for i in checks_list:
    #     if i['user_ID'] == inputID :
    #         check_ID = True
    #         break
    # if check_ID:
    #     return templates.TemplateResponse(name="user/user_joincheck_ID.html", context={'request':request, 'check_ID':check_ID})
    # else: 
    #     return templates.TemplateResponse(name="user/user_joincheck_ID.html", context={'request':request})


    # for i in checks_list:
    #     if inputID == i["user_ID"]:
    #         check_ID = 1
    #     else : 
    #         check_ID = 0
    # if check_ID == 1:
    #     return templates.TemplateResponse(name="user_joincheck_ID.html", context={'request':request})
    # else: 
    #     return templates.TemplateResponse(name="user_joincheck_ID.html", context={'request':request})

# 회원가입 페이지 이메일 확인
    

@router.get("/user_joincheck_email", response_class=HTMLResponse) 
async def mypage(request:Request):
    pass
    return templates.TemplateResponse(name="user/user_joincheck_email.html", context={'request':request})

@router.post("/user_joincheck_email", response_class=HTMLResponse) 
async def mypage(request:Request):
    form_data = await request.form()
    dict_form_data = dict(form_data)
    inputemail = dict_form_data['user_email']

    check_list = await collection_member.get_all()
    checks_list = [check.dict() for check in check_list]

    check_email = False
    pass
    for i in checks_list:
        if i['user_email'] == inputemail :
            check_email = True
            break

    return templates.TemplateResponse(name="user/user_joincheck_email.html", context={'request':request, 'check_email' : check_email})

# 로그인
@router.get("/user_login", response_class=HTMLResponse) 
async def user_login(request:Request):
    return templates.TemplateResponse(name="user/user_login.html", context={'request':request})

@router.post("/user_login", response_class=HTMLResponse) 
async def user_login(request:Request):
    return templates.TemplateResponse(name="user/user_login.html", context={'request':request})

# 로그인 체킹 페이지
@router.get("/user_logincheck", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_logincheck.html", context={'request':request})

@router.post("/user_logincheck", response_class=HTMLResponse) 
async def mypage(request:Request):
    form_data = await request.form()
    dict_form_data = dict(form_data)
    pass
    inputID = dict_form_data['user_ID']
    inputPSWD = dict_form_data['user_pswd']

    check_list = await collection_member.get_all()
    checks_list = [answer.dict() for answer in check_list]

    logcheck = False
    pass
    for i in checks_list:
        if i['user_ID'] == inputID and i['user_pswd'] == inputPSWD:
            logcheck = True
            break
    if logcheck:
        return templates.TemplateResponse(name="mainpage.html", context={'request':request})
    else: 
        return templates.TemplateResponse(name="user/user_logincheck.html", context={'request':request})


# 마이 페이지
@router.get("/user_mypage", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_mypage.html", context={'request':request})

@router.post("/user_mypage", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_mypage.html", context={'request':request})


# 아이디/비밀번호 찾기
@router.get("/user_infosearch", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_infosearch.html", context={'request':request})

@router.post("/user_infosearch", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_infosearch.html", context={'request':request})


# 이용약관
@router.get("/user_privacypolicy", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_privacypolicy.html", context={'request':request})

@router.post("/user_privacypolicy", response_class=HTMLResponse) 
async def mypage(request:Request):
    return templates.TemplateResponse(name="user/user_privacypolicy.html", context={'request':request})