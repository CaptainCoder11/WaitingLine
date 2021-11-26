from .config import config
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print(config.url)

engine=create_engine(config.url,echo=True)

Base = declarative_base()

SessionLocal=sessionmaker(bind=engine)