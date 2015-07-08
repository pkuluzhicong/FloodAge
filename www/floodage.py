#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
import time

def clamp(minimum, x, maximum):
	return max(minimum, min(x, maximum))

class _Construction(object):
	def __init__(self, name, cost):
		self.name = name
		self.level = 0
		self.cost = cost  #基本消耗，格式:(木，石，粮, 时间）

	def price(self):
		return (level*level*cost[0],level*level*cost[1],level*level*cost[2],level*level*cost[3])

class _City:
	

	def __init__(self):
		self.type_=0 #城市类型为0表示是空地

	def isEmpty(self):
		return self.type_==0

	def activate(self, name, type_=1):
		if(type_ == 0):
			return False
		if(self.type_ != 0):
			return 'Cannot Activate again'
		self.type_ = type_
		self.name = name
		
		if(type_ == 1): 
			self.buildings={'Minicipal':_Construction('Minicipal', cost=(100,100,100,10)),
							'Barracks':_Construction('Barracks', cost=(50,40,25,9)),
							'Storage':_Construction('Storage',cost=(40,50,25,9)),
							'Farm':_Construction('Farm',cost=(40,40,25,8)),
							'Digging':_Construction('Digging',cost=(40,25,40)),
							'Mill':_Construction('Mill',cost=(25,40,40))
							}
			
			self.grass=300
			self.wood=300
			self.stone=300
			self.population=0
			self.diamond=5
			
			self.infantry=0
			self.cavalry=0
			self.archer=0
			
		self.update_level()

	def update_level(self): #更新与建筑等级相关的属性
		self.level = self.buildings['Minicipal'].level
		self.maxPopulation=self.buildings['Barracks'].level * 30
		self.maxResource=self.buildings['Storage'].level * self.buildings['Storage'].level * 200 
		self.woodPerMin=self.buildings['Mill'].level * self.buildings['Mill'].level * 30
		self.stonePerMin=self.buildings['Digging'].level *self.buildings['Digging'].level *30
		self.grassPerMin=self.buildings['Farm'].level * self.buildings['Farm'].level *40
		
	def update_resource(self):
		self.change_resource(self.woodPerMin,self.stonePerMin,self.grassPerMin)
		
	def change_resource(self,w,s,g,d=0):
		self.wood=clamp(0,self.wood+w,self.maxResource)
		self.stone=clamp(0,self.stone+s,self.maxResource)
		self.grass=clamp(0,self.grass+g,self.maxResource)
		self.diamond= max (0,self.diamond+d)
		
	def change_army(self,i,c,a):
		self.infantry=max(0,self.infantry+i)
		self.cavalry=max(0,self.cavalry+c)
		self.archer=max(0,self.archer+a)

class Floodage:
	def __init__(self, lineNum, colNum):
		self.cityList=[ [] for i in range(lineNum) ]
		self.lineNum=lineNum
		self.colNum=colNum
		for i in range(lineNum):
			for j in range(colNum):
				self.cityList[i].append(_City())

	def update(self):
		for i in range(self.lineNum):
			for j in range(self.colNum):
				if not self.cityList[i][j].isEmpty():
					self.cityList[i][j].update_level()
					self.cityList[i][j].update_resource()
	
	def activate_city(self,position,name,type_=1):
		self.cityList[position[0]][position[1]].activate(name,type_)

	def query_city(self,position):
		if not self.cityList[position[0]][position[1]].isEmpty():
			return self.cityList[position[0]][position[1]]
		
	def levelup_building(self,position,building):
		if not self.cityList[position[0]][position[1]].isEmpty():
			self.cityList[position[0]][position[1]].buildings[building].level+=1
			self.cityList[position[0]][position[1]].update_level()
		
	def change_resource(self,position,w,s,g,d=0):
		if not self.cityList[position[0]][position[1]].isEmpty():
			self.cityList[position[0]][position[1]].change_resource(w,s,g,d)
		
	def change_army(self,position,i,c,a):
		if not self.cityList[position[0]][position[1]].isEmpty():
			self.cityList[position[0]][position[1]].change_army(i,c,a)

f=Floodage(6,7)
f.activate_city((2,3),'1')
f.query_city((2,3))
f.levelup_building((2,3),'Mill')
f.change_resource((1,2),5,5,5,5)
f.change_army((1,2),2,3,4)
