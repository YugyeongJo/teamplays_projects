from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class members(Document):
    user_ID: Optional[str] = None
    user_pswd: Optional[str] = None
    user_email: Optional[EmailStr] = None    
    user_name: Optional[str] = None
    user_info : Optional[str] = None
    user_birth : Optional[int] = None
    user_address : Optional[str] = None
    user_phone : Optional[int] = None
    
  
    class Settings:
        name = "members"