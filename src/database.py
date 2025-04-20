from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus
from .config import DATABASE_URL

# Create engine with fast_executemany for better bulk insert performance
engine = create_engine(
    DATABASE_URL,
    fast_executemany=True,
    connect_args={
        'TrustServerCertificate': 'yes'  # For development/testing. Remove in production if not needed
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 