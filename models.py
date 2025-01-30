from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str
    
class UserResponses(BaseModel):
    access_token:str
    token_type:str
    username:str