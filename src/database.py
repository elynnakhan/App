import os
from sqlalchemy import create_engine
import sqlalchemy.ext.declarative as _declarative
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Read the DATABASE_URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")
#DATABASE_URL = "mysql+pymysql://root:123@localhost:3306/TestApplication"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
