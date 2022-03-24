from pydantic import BaseModel
from datetime import date, datetime
class UserBase(BaseModel):
    username :str
    email : str
    password : str


class UserDisplay(BaseModel):
    username :str
    email : str

    class Config():
        orm_mode = True

class PostBase(BaseModel):
    image_url : str
    image_url_type : str
    caption : str
    creater_user : str

class User(BaseModel):
    username : str
    class Config():
        orm_mode = True

class PostDisplay(BaseModel):
    id : int
    image_url : str
    image_url_type : str
    caption : str
    timestamp : datetime
    user : User

    class Config():
        orm_mode = True

class UserAuth(BaseModel):
    id : int
    username : str
    email : str

class Comment(BaseModel):
    text : str
    username : str
    timestamp : datetime
    
    class Config():
        orm_mode = True

class CommentBase(BaseModel):
    username : str
    text : str
    post_id : int