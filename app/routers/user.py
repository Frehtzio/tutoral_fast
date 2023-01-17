from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas,utils
from ..database import engine, get_db

router = APIRouter(
    prefix="/user",
    tags=['User']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Outuser)
def create_user(user: schemas.CreateUser,db: Session = Depends(get_db)):
    hased_password = utils.hash(user.password)
    user.password= hased_password
    print(hased_password)

    new_user = models.User(**user.dict())
    #new_posts = models.Post(title = post.title,content = post.content,published=post.valid)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    
    return new_user


@router.get("/{id}")
def get_user(id:int,db: Session = Depends(get_db)):
    print("hola")
    user = db.query(models.User).filter(models.User.user_id == id).first()
    if not user:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with {id} does not exist"))
    return user