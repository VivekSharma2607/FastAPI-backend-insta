from fastapi import HTTPException ,status
from starlette import status
from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from db.hashing import Hash
from db.models import DBUser
def create_user(db : Session , request : UserBase):
    new_User = DBUser(
        username = request.username,
        email = request.email ,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_User)
    db.commit()
    db.refresh(new_User)
    return new_User


def get_user_by_username(db : Session , username : str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with username {username} not found')
    return user