from routers.schemas import Comment, CommentBase , UserAuth
from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_comment
from auth.autho import get_current_user
router = APIRouter(
    prefix='/comment',
    tags=['comment']
)
@router.get('/all/{post_id}')
def comment(post_id : int , db : Session = Depends(get_db)):
    return db_comment.get_all(db,post_id)

@router.post('')
def create(request : CommentBase , db : Session = Depends(get_db) , current_user : UserAuth = Depends(get_current_user)):
    return db_comment.create(db,request)