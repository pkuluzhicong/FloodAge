#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column,ForeignKey, Integer, String,DateTime
from database import Base
from datetime  import datetime,timedelta

class User(Base):
    __tablename__ = 'user'
    __table_args__={'extend_existing':True}
    username = Column(String(30), primary_key=True)
    passwd = Column(String(30))

    def __init__(self, username=None, passwd=None):
        self.username = username
        self.passwd = passwd

    def __repr__(self):
        return '<User %r>' % (self.username)
        

class City(Base):
    __tablename__ = 'city'
    __table_args__={'extend_existing':True}
    username = Column(String(30))
    posX = Column(Integer,primary_key=True)
    posY = Column(Integer,primary_key=True)
    grass = Column(Integer,default=300)
    wood = Column(Integer,default=300)
    stone = Column(Integer,default=300)
    infantry = Column(Integer,default=0)
    cavalry = Column(Integer,default=0)
    archer = Column(Integer,default=0)
    minicipal = Column(Integer,default=1)
    barracks = Column(Integer,default=0)
    storage = Column(Integer,default=0)
    farm = Column(Integer,default=0)
    digging = Column(Integer,default=0)
    mill = Column(Integer,default=0)
    
    def __init__(self,username,posX,posY):
        self.username=username
        self.posX=posX
        self.posY=posY
        
    def __repr__(self):
        return '<Position %r%r>' % (self.posX,self.posY)
        
    def print_(self):
        print self.posX,self.posY
    
class Message(Base):
    __tablename__ = 'message'
    __table_args__={'extend_existing':True}
    messageId = Column(Integer,primary_key=True)
    username = Column(String(30))
    sendername = Column(String(30))
    begin_time = Column(DateTime)    
    end_time = Column(DateTime)
    title = Column(String(30))
    status = Column(Integer,default = 0) #0是未完成，1是完成，-1是取消
    detail = Column(String(140))
    
    def __init__(self,messageId,username,sendername,delta_second,title):
        self.messageId=messageId
        self.username=username
        self.sendername=sendername
        self.begin_time = datetime.now()
        self.end_time = datetime.now() + timedelta(seconds=delta_second)
        self.title=title
        self.detail=''
    
    def __repr__(self):
        return '<Message %r>' % (self.messageId)
    
    def print_(self):
        print self.messageId,self.username,self.sendername,self.begin_time,self.end_time,self.title,self.status,self.detail
    
    
    

