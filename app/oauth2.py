from jose import JWSError,jwt, exceptions
from datetime import datetime,timedelta
from . import schemas
from fastapi import Depends, HTTPException, status
from . import database,models

from fastapi.security import OAuth2PasswordBearer
from .config import settings

# creating tokken


# el tokenurl tiene que tener el path del login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2Njk5OTU3NDh9.teu3piilK8wCTfZwKDnB_oEHXR9hNO8swK0zgVCsOkE

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES



def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() +timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp":expire})
    
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def verify_access_token(token:str, credentials_exception):
   
    try:
    

        payload =jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHM])
        
        id : str = payload.get("user_id")
        
        
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except exceptions.JWSError:
      
        #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzA0MzUwNjJ9.bsikmzXI77YeRO3Uv2J_oEsBuT4RxyAkGZqvUWr9aB4
        
        raise credentials_exception
    
    return token_data
    
    
def get_current_user(token : str = Depends(oauth2_scheme),db: str = Depends(database.get_db)):
    


    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate credentials",
                                          headers={"WWW-Authenticate":"Bearer"})
    
    token = verify_access_token(token,credentials_exception)
    
    user = db.query(models.User).filter(models.User.user_id == token.id).first()
    #print(user.user_id)
    
   
    

    return user
