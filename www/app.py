@celery.task()
def recruit_archer_done(mesId,x,y,num,timedelta):
    time.sleep(timedelta)
    mes = Message.query.filter(Message.messageId==mesId).first()
    if( mes is not None and mes.status != -1):
        mes.status = 1
        City.query.filter(City.posX==x and City.posY ==y).first().archer+=num
    db_session.commit()
    
