from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class User(Document):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    pswd: Optional[str] = None
    manager: Optional[str] = None
    sellist1 : Optional[str] = None
    text : Optional[str] = None
  
    class Settings:
        name = "users"