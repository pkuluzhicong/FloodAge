#-*- coding: UTF-8 -*- 

#数据库基类, 建立数据库需要import这里的init_db函数并执行


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/FloodAge.db', convert_unicode=True)
#engine = create_engine('sqlite:////home/bylcc/FloodAge/www/db/game.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    import models
    Base.metadata.create_all(bind=engine)
