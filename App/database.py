from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
import app.config as config

# Create the engine
engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite-specific
    echo=False,
    future=True,
)

# Create a configured "Session" class
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))

# Create a Base class for declarative models
Base = declarative_base()
