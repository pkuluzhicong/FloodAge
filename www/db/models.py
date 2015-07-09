
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
        return 'User: %s, Passwd: %s' % (self.username,self.passwd)
        

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
    barracks = Column(Integer,default=1)
    storage = Column(Integer,default=1)
    farm = Column(Integer,default=1)
    digging = Column(Integer,default=1)
    mill = Column(Integer,default=1)
    
    BasicPrice={'minicipal':(200,200,200,10),'barracks':(100,100,50,9),'storage':(100,100,50,9),'farm':(80,80,50,8),'digging':(80,80,50,8),'mill':(80,80,50,8),'infantry':(40,40,80,5),'cavalry':(50,50,100,6),'archer':(30,30,60,5)}
    
    BasicProduction={'grass':40,'wood':30,'stone':30}
    
    BasicAbility={'infantry':(8,8,8),'cavalry':(10,6,10),'archer':(6,10,6)} #兵种属性值：（攻击，防御，速度）
    
    
    def __init__(self,username,posX,posY):
        self.username=username
        self.posX=posX
        self.posY=posY
        
    def __repr__(self):
        return 'User: %r, Position: (%r,%r)' % (self.username,self.posX,self.posY)
    
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
    event = Column(String(10))
    title = Column(String(30))
    status = Column(Integer,default = 0) #0是未完成，1是完成，-1是取消
    detail = Column(String(140))
    
    def __init__(self,messageId,username,sendername,delta_second,event,title):
        self.messageId=messageId
        self.username=username
        self.sendername=sendername
        self.begin_time = datetime.now()
        self.end_time = datetime.now() + timedelta(seconds=delta_second)
        self.event=event
        self.title=title
        self.detail=''
    
    def __repr__(self):
        return 'Message %r' % (self.messageId)
    
    def print_(self):
        print self.messageId,self.username,self.sendername,self.begin_time,self.end_time,self.title,self.status,self.detail
    
    
    

