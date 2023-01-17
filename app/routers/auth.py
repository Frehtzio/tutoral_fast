from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm # esto hace que ya no se espere un json sino un form-data
from sqlalchemy.orm import Session
from ..database import engine, get_db
from .. import schemas,models,utils,oauth2



router = APIRouter(tags=["Auth"])
#user_credentials: schemas.UserLogin    
@router.post("/login",response_model= schemas.Token)

#OAuth2PasswordRequestForm = Depends()
def login(user_credentials:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials ")

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials ")
 
    access_token =  oauth2.create_access_token(data = {"user_id":user.user_id})
    
    
    #create token 
    # return token
    return  {"access_token":access_token,"token_type":"bearer"}