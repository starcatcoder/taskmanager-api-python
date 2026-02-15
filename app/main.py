from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .database import engine, Base, SessionLocal
from . import models, schemas, auth

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependência para pegar sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================
# 🔐 ROTA DE REGISTRO
# ==========================
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Verifica se usuário já existe
    existing_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Criptografa senha
    hashed_password =_
