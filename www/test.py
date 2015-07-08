#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db.database import init_db

import os
os.system('rm db/game.db')
init_db()

from db.database import db_session
from db.models import *

x = User('fffx','123')
db_session.add(x)
b = City('fffx',1,7)
db_session.add(b)
b.print_()
c = Message(1245,'luzhicong','system',10,'Hello')
c.print_()
db_session.commit()
print City.query.all()
