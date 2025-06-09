from pydantic import  BaseModel
from app.schemas.users import UserOut

class ResponseLoggin(BaseModel):
    user: UserOut
    access_token: str

class AccessTokenResponse(BaseModel):
    access_token: str
