# 初始化sqlite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.model_insstar import Base
from model import SQL_SHOW

engine = create_engine('sqlite:///image', echo=SQL_SHOW)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)