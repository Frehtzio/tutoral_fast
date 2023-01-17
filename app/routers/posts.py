
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from typing import Optional,List
from sqlalchemy.orm import Session
# this will ge the func count and others
from sqlalchemy import func
from .. import models, schemas,utils
from ..database import engine, get_db
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

#response_model=List[schemas.Post]
#List[schemas.Post]
@router.get("/")
#                                                    NOTEE : this int its actually not doing anything 
def get_posts(db: Session = Depends(get_db),limit :int = 10,skip:int = 0,search : str |None = ""):
    # print(search) get_current_user : int = Depends(get_current_user)
    
    #post = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    #                                                         in label you can put wathever name you want
    results = db.query(models.Post,func.count(models.Vote.post_id).label("vote")).join(
        models.Vote,models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
            models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    
    # return an intance in models.Post in form  of orm  to sql


   
    
    
    return results

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post,)
def create_posts(post: schemas.CretePost,db: Session = Depends(get_db),get_current_user : int = Depends(get_current_user)):
    #cursor.execute(""" INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING * """,(post.title,post.content,post.valid))
    #lol = cursor.fetchone()
    #conn.commit()
   
    
    new_posts = models.Post(owner_id = get_current_user.user_id,  **post.dict())
    #new_posts = models.Post(title = post.title,content = post.content,published=post.valid)
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    #print(new_posts)
    
    return new_posts

@router.get("/{id}",response_model=schemas.PostOut)
def get_one_post(id:int,db: Session = Depends(get_db,), get_current_user : int = Depends(get_current_user)):
    
    #cursor.execute("""SELECT * FROM posts WHERE id = %s""" , str(id)) 
    #result = cursor.fetchone()
    #result = db.query(models.Post).filter(models.Post.id == id).first()
    
    result = db.query(models.Post,func.count(models.Vote.post_id).label("vote")).join(
        models.Vote,models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
            models.Post.id == id).first()
    
    
    
    if not result:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id of {id} does not exist "))
    return result


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)

def delete_post(id:int,db: Session = Depends(get_db),get_current_user : int = Depends(get_current_user)):
    #cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """ % str(id),)
    #post = cursor.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found"))
    if post.owner_id != get_current_user.user_id:
        raise(HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action"))
    
    #conn.commit()
    
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.Post)

def update_post(id:int,updated_post:schemas.PostCreated ,db: Session = Depends(get_db),get_current_user : int = Depends(get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    
    if post_query.first() == None:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found"))
    if post.owner_id != get_current_user.user_id:
        raise(HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you are not the creator of the post"))
    
    
    

    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    #print(post.first())
    return post_query.first()