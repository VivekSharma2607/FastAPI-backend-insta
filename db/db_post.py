import datetime

from fastapi import HTTPException , status
from sqlalchemy.sql.functions import user
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DBPost

def create(db : Session , request : PostBase):
    new_post = DBPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.datetime.now(),
        user_id = request.creater_user
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db:Session):
    return db.query(DBPost).all()

def delete(db:Session , id:int , user_id : int):
    post = db.query(DBPost).filter(DBPost.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail=f'Post with id {id} not found')
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail= 'Only Post creater can delete the Psot')

    db.delete(post)
    db.commit()
    return  'OK'   