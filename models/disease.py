from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class diseases(Document):
    dise_url : Optional[str] = None
    # dise_name: Optional[str] = None
    # dise_symp: Optional[EmailStr] = None
    # dise_affected: Optional[str] = None
    # dise_causes: Optional[str] = None
    # dise_diagn : Optional[str] = None
    # dise_cure : Optional[str] = None
    # dise_code : Optional[int] = None
  
    class Settings:
        name = "diseases"