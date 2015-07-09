import time
from celery import Celery
from celery.task.base import periodic_task
from datetime import timedelta
from math import sqrt
#from sqlalchemy import and_



CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}

from db.database import init_db
from db.database import db_session
from db.models import *

init_db()

#db_session.add(City('Zl',3,4))
#db_session.add(City('Lzc',2,3))
#db_session.commit()

celery = Celery('tasks', broker='redis://localhost:6379/0')


@celery.task()
def level_up_barracks_done(mesId,x,y):#升级兵营完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY== y).first(). barracks+=1
    db_session.commit()

@celery.task()
def level_up_storage_done(mesId,x,y):#升级仓库完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY== y).first(). storage+=1
    db_session.commit()

@celery.task()
def level_up_minicipal_done(mesId,x,y):#升级市政厅完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY== y).first(). minicipal+=1
    db_session.commit()
    
@celery.task()
def level_up_farm_done(mesId,x,y):#升级农场完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY== y).first(). farm+=1
    db_session.commit()

@celery.task()
def level_up_digging_done(mesId,x,y):#升级矿洞完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY== y).first(). digging+=1
    db_session.commit()
    
@celery.task()
def level_up_mill_done(mesId,x,y):#升级伐木场完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY== y).first(). mill+=1
    db_session.commit()

@celery.task()
def recruit_infantry_done(mesId,x,y,num):#招募步兵完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY ==y).first().infantry+=num
    db_session.commit()

@celery.task()
def recruit_cavalry_done(mesId,x,y,num):#招募骑兵完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY ==y).first().cavalry+=num
    db_session.commit()
    
@celery.task()
def recruit_archer_done(mesId,x,y,num):#招募弓箭手完成事件
    #time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY ==y).first().archer+=num
    db_session.commit()
    
@celery.task()
def attack_battle(mesId1,mesId2,attackerPosX,attackerPosY,defenserPosX,defenserPosY,infantryNum,cavalryNum,archerNum):#战斗事件，决定胜负，损失士兵数和战利品数
    countdown_ =  int(sqrt(attackerPosX*attackerPosX+attackerPosY*attackerPosY)*300)
    timedelta_ = timedelta(seconds = countdown_)
    #time.sleep(timedelta)
    #attacker = City.query.filter(and_(City.posX == attackerPosX, City.posY == attackerPosY)).first()
    #defenser = City.query.filter(and_(City.posX == defenserPosX, City.posY == defenserPosY)).first()
    attacker = City.query.filter((City.posX == attackerPosX) & (City.posY == attackerPosY)).first()
    defenser = City.query.filter((City.posX == defenserPosX) & (City.posY == defenserPosY)).first()
    
    mes1 = Message.query.filter(Message.messageId==mesId1).first()
    mes2 = Message.query.filter(Message.messageId==mesId2).first()
    
    mes1.status = 1
    mes2.status = 1
    
    wood=0
    stone=0
    grass=0
    
    attack_point = City.BasicAbility['infantry'][0]*infantryNum + City.BasicAbility['cavalry'][0]*cavalryNum + City.BasicAbility['archer'][0]*archerNum
    defense_point = City.BasicAbility['infantry'][1]*defenser.infantry + City.BasicAbility['cavalry'][1]*defenser.cavalry + City.BasicPrice['archer'][1]*defenser.archer
    if attack_point > defense_point:
        defenser.infantry/=4
        defenser.cavalry/=4
        defenser.archer/=4
        db_session.flush()
        infantryNum = max(infantryNum/4, infantryNum - defenser.infantry)
        cavalryNum = max(cavalryNum/4, cavalryNum - defenser.cavalry)
        archerNum = max(archerNum/4, archerNum - defenser.archer)
        mes1.detail = 'Victory!\nYour Survivors: Infantry %d, Cavalry %d, Archer %d\nEnermy Survivors: Infantry %d, Cavalry %d, Archer %d' % (infantryNum,cavalryNum,archerNum,defenser.infantry,defenser.cavalry,defenser.archer) 
        mes2.detail = 'Defeat!\nYour Survivors: Infantry %d, Cavalry %d, Archer %d\nEnermy Survivors: Infantry %d, Cavalry %d, Archer %d' %(defenser.infantry,defenser.cavalry,defenser.archer,infantryNum,cavalryNum,archerNum)
        
        wood=defenser.wood/2
        stone=defenser.stone/2
        grass=defenser.grass/2
        defenser.wood -= wood
        defenser.stone -= stone
        defenser.grass -= grass
        
    else:
        infantryNum/=4
        cavalryNum/=4
        archerNum/=4
        defenser.infantry = max(defenser.infantry/4, defenser.infantry - infantryNum)
        defenser.cavalry = max(defenser.cavalry/4, defenser.cavalry - cavalryNum)
        defenser.archer = max(defenser.archer/4,defenser.archer - archerNum)
        mes1.detail = 'Defeat!\nYour Survivors: Infantry %d, Cavalry %d, Archer %d\nEnermy Survivors: Infantry %d, Cavalry %d, Archer %d' % (infantryNum,cavalryNum,archerNum,defenser.infantry,defenser.cavalry,defenser.archer) 
        mes2.detail = 'Victory!\nYour Survivors: Infantry %d, Cavalry %d, Archer %d\nEnermy Survivors: Infantry %d, Cavalry %d, Archer %d' %(defenser.infantry,defenser.cavalry,defenser.archer,infantryNum,cavalryNum,archerNum)
        
    mesId = len(Message.query.all())+1
    mes = Message(mesId,attacker.username,'system',timedelta_,'Come Back','Come Back: Infantry %d, Cavalry %d, Archer %d'%(infantryNum,cavalryNum,archerNum))
    mes.detail = 'Spoils: Wood %d , Stone %d, Grass  %d' % (wood,stone,grass)
    db_session.add(mes)
    db_session.commit()
    #attack_return.delay(mesId,attackerPosX,attackerPosY,infantryNum,cavalryNum,archerNum,wood,stone,grass,timedelta)
    attack_return.apply_async(args=[mesId,attackerPosX,attackerPosY,infantryNum,cavalryNum,archerNum,wood,stone,grass],countdown=countdown_)
    
@celery.task()
def attack_return(mesId, x, y, infantryNum,cavalryNum,archerNum,wood,stone,grass):#战斗后攻击方返回事件，带回士兵和资源
    #time.sleep(timedelta)
    
    mes = Message.query.filter(Message.messageId==mesId).first()
    mes.status = 1
    
    city =  City.query.filter(City.posX==x and City.posY== y).first()
    city.infantry += infantryNum
    city.cavalry += cavalryNum
    city.archer += archerNum
    city.wood += wood
    city.stone += stone
    city.grass += grass
    
    db_session.commit()
    
    
    
    
@periodic_task(run_every=timedelta(seconds=60)) #每分钟执行一次，更新各城市的资源
def update():
    for instance in City.query.all():
        limit = (instance.storage + 1) * 500
        instance.grass = min((instance.grass + City.BasicProduction['grass']),limit)
        instance.wood = min((instance.wood + City.BasicProduction['wood']),limit)
        instance.stone = min((instance.stone + City.BasicProduction['stone']),limit)
    db_session.commit()
    for instance in City.query.all():
        print instance.username,instance.posX,instance.posY,instance.grass,instance.wood,instance.stone


    
