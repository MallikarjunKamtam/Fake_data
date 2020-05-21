import Names
import format
import Cities
import random
from Names import names
from format import Data
from Cities import cities

"""-----------------------------------------NAME-----------------------------------------"""
name = names.splitlines(0)
x = random.randint(1, 32000)
name_1 = name[x]

"""-----------------------------------------BIRTH_YEAR-----------------------------------------"""
by = random.randint(1997, 2010)
age = 2020 - by

if age > 18:
    stage = "Adult"
elif age in range(13, 18):
    stage = "Teenager"
else:
    stage = "Child"
"""-----------------------------------------PLACE-----------------------------------------"""
citi = cities.splitlines(0)
y = random.randint(1, 538)
citi_1 = citi[y]

student1 = Data(name_1, by, citi_1, 20)
print(f"Name: {student1.name},      " f'Age: {age}      ' f"Place: {citi_1}      ", f"Birth_year: {student1.birth_year }", f"        {stage}")