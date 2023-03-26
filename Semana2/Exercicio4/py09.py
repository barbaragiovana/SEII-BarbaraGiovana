# import my_module
# import my_module as mm
# from my_module import find_index as fi, test
# from my_module import *
from my_module import find_index, test

import sys

import random

import math

import datetime
import calendar

import os

courses = ['History', 'Math', 'Physics', 'CompSci']

# index = my_module.find_index(courses, 'Math')
# index = mm.find_index(courses, 'Math')
# index = fi(courses, 'Math')
index = find_index(courses, 'Math')
print(index)
print(test)

print(sys.path)

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)
print(calendar.isleap(2017))
print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)
