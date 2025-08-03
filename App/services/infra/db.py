# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
import app.config as config

# Create engine (adjust for Postgres if needed)
engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in config.SQLALCHEMY_DATABASE_URL else {},
    echo=False,
    future=True,
)

# Create session factory
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))

# Declarative base for models
Base = declarative_base()

# Session helpers
def get_session():
    return SessionLocal()

def close_session(session):
    session.close()
