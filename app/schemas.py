from pydantic import BaseModel,EmailStr
from enum import Enum, IntEnum
from typing import Optional
from datetime import datetime
class PostBase(BaseModel):
    title: str
    content:str
    published: bool = True
    #rating:Optional[int] = None

    
    
class CretePost(PostBase):
    pass

    
class Outuser(BaseModel):
    email:EmailStr
    user_id : int
    created_at: datetime

    class Config:
        orm_mode = True
        

class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int 
    owner : Outuser
  
    class Config:
        orm_mode = True
        
class PostOut(BaseModel):
    Post : Post
    vote : int
    
    class Config:
        orm_mode = True


        # this will convert to omr and when its return to the user will conver into a json
        
class PostCreated(PostBase):
    pass

        
        

class CreateUser(BaseModel):
    email :EmailStr
    password : str
    
    

        
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

class Token(BaseModel):
    access_token : str
    token_type: str
    

class TokenData(BaseModel):
    id: Optional[int] = None
    



class ZeroOneEnum(IntEnum):
    ZERO = 0
    ONE = 1

class Vote(BaseModel):
    post_id : int
    dir: ZeroOneEnum
