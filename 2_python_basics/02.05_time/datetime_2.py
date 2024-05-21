""" What is a class?

-A blue print or tewmplete for creating objects.

-It defines attributes and methods that are common to all objects of that class

""" 

class Car:
    def __init__(self, doors, model, year):
        self.doors = doors
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, speed_delta):
        self.speed += speed_delta

    def brake(self, speed_delta):
        if self.speed - speed_delta < 0:
            self.speed = 0
        else :
            self.speed -= speed_delta
            

# Modules, math, random

from math import pi

# Datetime module

import datetime

import time
time.time()

print(type(datetime.datetime))

print(time.ctime(time.time())) #curretn time

# The datetime modul

#- Get the datetime object of the current time of a given time:

from datetime import datetime


s = time.time()
t = time.time()

s == t

import datetime

dt_1 = datetime.datetime.today()
dt_2 = datetime.datetime.now()

print(dt_1)
print(dt_2)

