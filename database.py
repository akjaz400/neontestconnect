from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace this with your actual connection string from the Neon dashboard
DATABASE_URL = "postgresql://username:password@your-neon-host.neon.tech/neondb?sslmode=require"

# Create the engine (Neon works seamlessly with standard SQLAlchemy engines)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a Sample Table
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

# Create tables in Neon automatically if they don't exist
Base.metadata.create_all(bind=engine)

# Dependency to yield database sessions to your API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
