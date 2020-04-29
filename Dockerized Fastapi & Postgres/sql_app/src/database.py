# IMPORT SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, create_database

# Create a database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@host.docker.internal:5432/database_name"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/database_name"

# Create the SQLAlchemy engine
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# if not database_exists(engine.url):
#     create_database(engine.url)

# Create a SessionLocal class whose instances are a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class from which will inherit classes that will be used to create database models (the ORM models)
Base = declarative_base()
