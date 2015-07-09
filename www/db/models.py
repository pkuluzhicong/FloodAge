# -*- coding: utf-8 -*-

#三张表: User, City, Message

from sqlalchemy import Column,ForeignKey, Integer, String,DateTime
from database import Base
from datetime  import datetime,timedelta

class User(Base):
    __tablename__ = 'user'
    __table_args__={'extend_existing':True}
    username = Column(String(30), primary_key=True) #用户名
    passwd = Column(String(30)) #口令

    def __init__(self, username=None, passwd=None):
        self.username = username
        self.passwd = passwd

    def __repr__(self):
        return 'User: %s, Passwd: %s' % (self.username,self.passwd)
        

class City(Base):
    __tablename__ = 'city'
    __table_args__={'extend_existing':True}
    username = Column(String(30)) #用户名
    posX = Column(Integer,primary_key=True) #横坐标
    posY = Column(Integer,primary_key=True) #纵坐标
    grass = Column(Integer,default=300) #粮草数
    wood = Column(Integer,default=300) #木材数
    stone = Column(Integer,default=300) #石料数
    infantry = Column(Integer,default=0) #步兵数
    cavalry = Column(Integer,default=0) #骑兵数
    archer = Column(Integer,default=0) #弓箭手数
    minicipal = Column(Integer,default=1) #市政厅等级
    barracks = Column(Integer,default=1) #兵营等级
    storage = Column(Integer,default=1) #仓库等级
    farm = Column(Integer,default=1) #农场等级
    digging = Column(Integer,default=1) #矿洞等级
    mill = Column(Integer,default=1) #伐木场等级
    
    #基础造价字典(静态)
    BasicPrice={'minicipal':(200,200,200,10),'barracks':(100,100,50,9),'storage':(100,100,50,9),'farm':(80,80,50,8),'digging':(80,80,50,8),'mill':(80,80,50,8),'infantry':(40,40,80,5),'cavalry':(50,50,100,6),'archer':(30,30,60,5)}
    
    #基础产出字典(静态)
    BasicProduction={'grass':40,'wood':30,'stone':30}
    
    #基础战斗力字典(静态)
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
    messageId = Column(Integer,primary_key=True) #消息Id
    username = Column(String(30)) #用户名
    sendername = Column(String(30)) #发送者姓名(目前版本都是来自'system')
    begin_time = Column(DateTime) #开始时间
    end_time = Column(DateTime) #结束时间
    event = Column(String(10)) #消息类型
    title = Column(String(30)) #消息标题
    status = Column(Integer,default = 0) #消息状态, 0是未完成，1是完成，-1是取消
    detail = Column(String(140)) #消息细节
    
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
    
    
    

