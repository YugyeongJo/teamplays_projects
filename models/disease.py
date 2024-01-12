from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class diseases(Document):
    # dise_KCD_code : Optional[str] = None
    # dise_spc_code : Optional[int] = None
    # dise_group : Optional[str] = None
    # dise_name_kr: Optional[str] = None
    # dise_name_en: Optional[str] = None
    # dise_symp: Optional[str] = None
    # dise_affected: Optional[str] = None
    # dise_causes: Optional[str] = None
    # dise_diagn : Optional[str] = None
    # dise_cure : Optional[str] = None
    dise_url : Optional[str] = None
  
    class Settings:
        name = "diseases"