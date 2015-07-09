from flask import render_template, session, redirect, url_for, escape, request,make_response,flash
from www import app
from API import *

import random

from db.database import db_session
from db.models import *

# close the db link 
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    
# the index: Login Page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Main Page of the Game: information of your city and the world map
@app.route('/fight')
def fight():
    return render_template('fight.html',UserName=session['username'],UserCity=UserCity(session['username']),Map=PosiName_Data())
    
#the Register Page
@app.route('/register')
def register():
    return render_template('register.html')
    
#Message Page of the Game:showing events finished , unfinished and canceled
@app.route('/mymsg')
def mymsg():
    return render_template('mymsg.html',UserName=session['username'],MsgQueue=MsgQueue(session['username']))

#the message list of a user
def MsgQueue(a):
    MyList = []
    MyList = Message.query.filter(Message.username == a).order_by(Message.messageId).all()
    return MyList
    
#the detail of a message
@app.route('/detail/<messageId>')
def detail(messageId):
    return render_template('detail.html',UserName=session['username'],dt_msg=dt_msg(messageId))
    
#get a piece of message by messageId
def dt_msg(b):
    return Message.query.filter(Message.messageId == b).first()

#City Pageof the Game:other city's information ,invade it!
@app.route('/incity')
@app.route('/incity/<cityname>')
def incity(cityname=None):
    if (cityname==None)and(session['cityname'] != None ):
        cityname = session['cityname']
        session.pop('cityname', None)
    return render_template('incity.html',UserName=session['username'],UserCity=UserCity(session['username']),Map=PosiName_Data(),OtherCity=UserCity(cityname),cityname=cityname)
    
#check if the password is coupled with the username
def valid_login(a,b):
    return User.query.filter(User.username == a).first().passwd == b
    
#check if the login-step is legal
@app.route('/logincheck', methods=['GET', 'POST'])
def logincheck():
    if request.method == 'POST':
        if request.form['username'] != "" :
            if request.form['password'] != "":
                if valid_login(request.form['username'],request.form['password']):
                    session['username'] = request.form['username']
                    return redirect(url_for('fight'))
                else :
                    error = 'Invalid username/password'
            else :
                error = 'the password has to be filled!'
        else :
            error = 'the username has to be filled!'
    return render_template('index.html', error=error)
    
# get a random position where there doesnot exists a city 
def posi_ram():
    a=0
    b=0
    while (City.query.filter((City.posX == a) and (City.posY == b) ).first() != None):
        a = random.randint(-1,10)
        b = random.randint(-1,18)
    return (a,b)
    
#check if the register-step is legal
@app.route('/registercheck', methods=['GET', 'POST'])
def registercheck():
    if request.method == 'POST':
        if request.form['username'] != "" :
            if request.form['password1'] != "":
                if request.form['password1'] == request.form['password2']:
                    if (User.query.filter(User.username== request.form['username'] ).first() == None):
                        NewUser=User(request.form['username'],request.form['password1'])
                        new_posi=posi_ram();
                        NewCity=City(request.form['username'],new_posi[0],new_posi[1])
                        db_session.add(NewUser)
                        db_session.add(NewCity)
                        db_session.commit()
                        return redirect(url_for('index'))
                    else:        
                        error = 'the user already exists!'
                else :
                    error = 'the password1 doesnot equal to password2!'
            else :
                error = 'the password has to be filled!'
        else :
            error = 'the username has to be filled!'
    return render_template('register.html', error=error)
    
#logout to the index 
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
    
#add a item to the constructing queue :minicipal
@app.route('/minicipal')
def minicipal():
    flash(level_up_minicipal(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))
    
#add a item to the constructing queue :barracks
@app.route('/barracks')
def barracks():
    flash(level_up_barracks(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))
    
#add a item to the constructing queue :storage
@app.route('/storage')
def storage():
    flash(level_up_storage(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))
    
#add a item to the constructing queue :farm
@app.route('/farm')
def farm():
    flash(level_up_farm(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))
    
#add a item to the constructing queue :digging
@app.route('/digging')
def digging():
    flash(level_up_digging(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))

#add a item to the constructing queue :mill
@app.route('/mill')
def mill():
    flash(level_up_mill(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))
    
#add a item to the recruit queue :infantry
@app.route('/infantry')
def infantry():
    flash(recruit_infantry(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))

#add a item to the recruit queue :cavalry
@app.route('/cavalry')
def cavalry():
    flash(recruit_cavalry(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))
    
#add a item to the recruit queue :archer
@app.route('/archer')
def archer():
    flash(recruit_archer(session['username'],UserCity(session['username']).posX,UserCity(session['username']).posY))
    return redirect(url_for('fight'))
    
#add a item to the attack queue 
@app.route('/invade', methods=['POST'])
def invade():
    flash(attack(UserCity(session['username']).posX,UserCity(session['username']).posY,UserCity(request.form['cityname']).posX,UserCity(request.form['cityname']).posY,request.form['infantry'],request.form['cavalry'],request.form['archer']))
    return redirect(url_for('fight'))
    
#cancel a item of the constructing queue
@app.route('/msgcancel/<messageId>')
def msgcancel(messageId):
    flash(cancel_event(messageId))
    return redirect(url_for('mymsg'))


#get the map :position and owner of city 
def PosiName_Data():
    MyList = {}
    for ele in City.query.all() :
        MyList[(ele.posX,ele.posY)]=ele.username
    return MyList
    
#get the city of a user 
def UserCity(a):
    return City.query.filter(City.username==a).first()
    
    
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    
