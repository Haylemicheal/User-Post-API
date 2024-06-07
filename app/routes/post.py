from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import PostCreate, Post
from app.crud import create_post, get_posts, delete_post
from app.database import get_db
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.post("/add", response_model=Post)
def add_post(post: PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_post(db=db, post=post, user_id=current_user.id)

@router.get("/", response_model=List[Post])
def get_user_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_posts(db=db, user_id=current_user.id)

@router.delete("/{post_id}", response_model=Post)
def delete_user_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = delete_post(db=db, post_id=post_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}
