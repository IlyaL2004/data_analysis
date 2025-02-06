import datetime
from pydantic import BaseModel, EmailStr

class VisitСheck(BaseModel):
    #id: int
    user_email: EmailStr
    site_id: int
    date: datetime.datetime
    admin_name: str

class VisitCreate(BaseModel):
    #id: int
    user_email: EmailStr
    site_id: int
    date: datetime.datetime
    admin_name: str
