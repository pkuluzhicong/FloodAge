from db.database import init_db
from db.database import db_session
from db.models import *
from tasks import *
#from sqlalchemy import and_
from math import sqrt

init_db()

####
#db_session.add(City('Zl',3,4))
#db_session.commit()
####


def showMessage():
    for item in Message.query.all():
        item.print_()

def clean():
    for instance in City.query.all():
        instance.grass=0
        instance.wood=0
        instance.stone=0
        instance.minicipal=3
        instance.storage=0
        db_session.commit()

def clean_message():
    for mes in Message.query.filter(Message.status==0).all():
        db_session.delete(mes)
        db_session.commit()

def level_up_minicipal(name,x,y):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
        
    cost = (city.minicipal*City.BasicPrice['minicipal'][0],city.minicipal*City.BasicPrice['minicipal'][1],city.minicipal*City.BasicPrice['minicipal'][2],city.minicipal*City.BasicPrice['minicipal'][3])
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name , Message.event == 'Level up' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event == 'Level up') & (Message.status==0)).first() is not None:
        return 'Fail: Another Construction Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Level up','Level up: Minicipal'))
    db_session.commit()
    #level_up_minicipal_done.delay(mesId,x,y,cost[3])
    level_up_minicipal_done.apply_async(args=[mesId,x,y], countdown=cost[3])
    return 'Success!'

def level_up_storage(name,x,y):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
    if city.storage >= city.minicipal:
        return 'Fail: Minicipal Level Too Low.'
    cost = (city.storage*City.BasicPrice['storage'][0],city.storage*City.BasicPrice['storage'][1],city.storage*City.BasicPrice['storage'][2],city.storage*City.BasicPrice['storage'][3])
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name, Message.event =='Level up' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event =='Level up') & (Message.status==0)).first() is not None:
        return 'Fail: Another Construction Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Level up','Level up: Storage'))
    db_session.commit()
    #level_up_storage_done.delay(mesId,x,y,cost[3])
    level_up_storage_done.apply_async(args=[mesId,x,y], countdown=cost[3])
    return 'Success!'
    
def level_up_barracks(name,x,y):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
    if city.barracks >= city.minicipal:
        return 'Fail: Minicipal Level Too Low.'
    cost = (city.barracks*City.BasicPrice['barracks'][0],city.barracks*City.BasicPrice['barracks'][1],city.barracks*City.BasicPrice['barracks'][2],city.barracks*City.BasicPrice['barracks'][3])
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name, Message.event =='Level up' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event =='Level up') & (Message.status==0)).first() is not None:
        return 'Fail: Another Construction Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Level up','Level up: Barracks'))
    db_session.commit()
    #level_up_barracks_done.delay(mesId,x,y,cost[3])
    level_up_barracks_done.apply_async(args=[mesId,x,y], countdown=cost[3])
    return 'Success!'
    
def level_up_farm(name,x,y):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
    if city.farm >= city.minicipal:
        return 'Fail: Minicipal Level Too Low.'
    cost = (city.farm*City.BasicPrice['farm'][0],city.farm*City.BasicPrice['farm'][1],city.farm*City.BasicPrice['farm'][2],city.farm*City.BasicPrice['farm'][3])
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name, Message.event =='Level up' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event =='Level up') & (Message.status==0)).first() is not None:
        return 'Fail: Another Construction Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Level up','Level up: Farm'))
    db_session.commit()
    #level_up_farm_done.delay(mesId,x,y,cost[3])
    level_up_farm_done.apply_async(args=[mesId,x,y], countdown=cost[3])
    return 'Success!'
    
def level_up_digging(name,x,y):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
    if city.digging >= city.minicipal:
        return 'Fail: Minicipal Level Too Low.'
    cost = (city.digging*City.BasicPrice['digging'][0],city.digging*City.BasicPrice['digging'][1],city.digging*City.BasicPrice['digging'][2],city.digging*City.BasicPrice['digging'][3])
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name, Message.event =='Level up' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event =='Level up') & (Message.status==0)).first() is not None:
        return 'Fail: Another Construction Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Level up','Level up: Digging'))
    db_session.commit()
    #level_up_digging_done.delay(mesId,x,y,cost[3])
    level_up_digging_done.apply_async(args=[mesId,x,y], countdown=cost[3])
    return 'Success!'
    
def level_up_mill(name,x,y):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
    if city.mill >= city.minicipal:
        return 'Fail: Minicipal Level Too Low.'
    cost = (city.mill*City.BasicPrice['mill'][0],city.mill*City.BasicPrice['mill'][1],city.mill*City.BasicPrice['mill'][2],city.mill*City.BasicPrice['mill'][3])
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name, Message.event =='Level up' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event =='Level up') & (Message.status==0)).first() is not None:
        return 'Fail: Another Construction Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Level up','Level up: Mill'))
    db_session.commit()
    #level_up_mill_done.delay(mesId,x,y,cost[3])
    level_up_mill_done.apply_async(args=[mesId,x,y], countdown=cost[3])
    return 'Success!'
    
def recruit_infantry(name,x,y,num=1):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
    if city.infantry+city.cavalry+city.archer+num > city.barracks*10:
        return 'Fail: Barracks Level Too Low.'
        
    cost = (City.BasicPrice['infantry'][0]*num,City.BasicPrice['infantry'][1]*num,City.BasicPrice['infantry'][2]*num,City.BasicPrice['infantry'][3]*num)
    
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name, Message.event =='Recruit' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event =='Recruit') & (Message.status==0)).first() is not None:
        return 'Fail: Another Recruit Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Recruit','Recruit: Infantry'))
    db_session.commit()
    #recruit_infantry_done.delay(mesId,x,y,num,cost[3])
    recruit_infantry_done.apply_async(args=[mesId,x,y,num], countdown=cost[3])
    return 'Success!'
    
def recruit_cavalry(name,x,y,num=1):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
    if city.cavalry+city.cavalry+city.archer+num > city.barracks*10:
        return 'Fail: Barracks Level Too Low.'
        
    cost = (City.BasicPrice['cavalry'][0]*num,City.BasicPrice['cavalry'][1]*num,City.BasicPrice['cavalry'][2]*num,City.BasicPrice['cavalry'][3]*num)
    
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name, Message.event =='Recruit' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event =='Recruit') & (Message.status==0)).first() is not None:
        return 'Fail: Another Recruit Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Recruit','Recruit: Cavalry'))
    db_session.commit()
    #recruit_cavalry_done.delay(mesId,x,y,num,cost[3])
    recruit_cavalry_done.apply_async(args=[mesId,x,y,num], countdown=cost[3])
    return 'Success!'
    
def recruit_archer(name,x,y,num=1):#
    #city = City.query.filter(and_(City.posX==x , City.posY==y)).first()
    city = City.query.filter((City.posX==x) & (City.posY==y)).first()
    if city is None:
        return 'Error: city not exist!'
    if city.archer+city.cavalry+city.archer+num > city.barracks*10:
        return 'Fail: Barracks Level Too Low.'
        
    cost = (City.BasicPrice['archer'][0]*num,City.BasicPrice['archer'][1]*num,City.BasicPrice['archer'][2]*num,City.BasicPrice['archer'][3]*num)
    
    if city.wood <= cost[0]:
        return 'Fail: Wood Not Enough'
    if city.stone <= cost[1]:
        return 'Fail: Stone Not Enough'
    if city.grass <= cost[2]:
        return 'Fail: Grass Not Enough'
    
    #if Message.query.filter(and_(Message.username == name, Message.event =='Recruit' , Message.status==0)).first() is not None:
    if Message.query.filter((Message.username == name) & (Message.event =='Recruit') & (Message.status==0)).first() is not None:
        return 'Fail: Another Recruit Exist' 
    
    print 'OK'
    
    city.wood-=cost[0]
    city.stone-=cost[1]
    city.grass-=cost[2]
    
    mesId = len(Message.query.all())+1
    db_session.add(Message(mesId,name,'system',cost[3],'Recruit','Recruit: Archer'))
    db_session.commit()
    #recruit_archer_done.delay(mesId,x,y,num,cost[3])
    recruit_archer_done.apply_async(args=[mesId,x,y,num], countdown=cost[3])
    return 'Success!'
    
def cancel_event(messageId):
    mes = Message.query.filter((Message.messageId == messageId) & (Message.status != 1)).first() 
    #if event != 'Attack' and event != 'Come Back':
        #mes = Message.query.filter(and_(Message.messageId == messageId , Message.status != 1)).first() 
        #mes = Message.query.filter((Message.messageId == messageId) & (Message.status != 1)).first() 
    if mes is not None:
        mes.status = -1
        db_session.commit()
        return 'Cancel Done'
    else:
        return 'Cancel Failed'
    
        
        
def attack(attackerPosX,attackerPosY,defenserPosX,defenserPosY,infantryNum,cavalryNum,archerNum):#
    #attacker = City.query.filter(and_(City.posX == attackerPosX, City.posY == attackerPosY)).first()
    attacker = City.query.filter((City.posX == attackerPosX) & (City.posY == attackerPosY)).first()
    #defenser = City.query.filter(and_(City.posX == defenserPosX, City.posY == defenserPosY)).first()
    defenser = City.query.filter((City.posX == defenserPosX) & (City.posY == defenserPosY)).first()
    
    if attacker is None or defenser is None:
        return 'Error: city not exist!'
    
    if attacker.infantry < infantryNum or attacker.cavalry < cavalryNum or attacker.archer<archerNum:
        return 'Fail: Army not enough'
    
    mesId1 = len(Message.query.all())+1
    mesId2 = mesId1 + 1
    #time_delta = timedelta(minutes = int(sqrt(attackerPosX*attackerPosX+attackerPosY*attackerPosY)*5))
    countdown_ =  int(sqrt(attackerPosX*attackerPosX+attackerPosY*attackerPosY)*300) #用于延时调用
    time_delta = timedelta(seconds = countdown_) #用于写入message
    
    
    db_session.add(Message(mesId1,attacker.name,'system',time_delta,'Attack','Attack: from '+attacker.name+' to ' + defenser.name))
    db_session.add(Message(mesId2,defenser.name,'system',time_delta,'Attack','Attack: from '+attacker.name+' to ' + defenser.name))
    db_session.commit()
    
    #attack_battle.delay(mesId1,mesId2,attackerPosX,attackerPosY,defenserPosX,defenserPosY,infantryNum,cavalryNum,archerNum,time_delta)
    attack_battle.apply_async(args=[mesId1,mesId2,attackerPosX,attackerPosY,defenserPosX,defenserPosY,infantryNum,cavalryNum,archerNum], countdown=countdown_)
    
    return 'Success!'
    
    
