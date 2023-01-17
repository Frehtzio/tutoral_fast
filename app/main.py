from fastapi import FastAPI
# lo de arriba es para que te lo pueda dar el nombre dela collumna 

from . import models

from .database import engine
from .routers import posts,user,auth,vote
from fastapi.middleware.cors import CORSMiddleware



#models.Base.metadata.create_all(bind=engine)
# esto de arriba ara que se cree la base de datos y si no pues ignora
# como estamos usando alembic ya no es necesario, note alembic es basicamente un actualizador de base de datos



app = FastAPI()
origins = ["https://www.google.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")

def hi():
    return {"message":"hello"}

    

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

