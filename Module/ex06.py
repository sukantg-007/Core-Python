from math import floor
import random
for i in range(1,3):
    print(random.random())
for i in range(1,3):
    print(random.randint(1,100))
for i in range(1,3):
    print(random.uniform(1,10))

for i in range(3):
    print(random.randrange(5))

for i in range(3):
    print(random.randrange(2,5))

for i in range(3):
    print(random.randrange(2,5,2))

list=[x for x in "abcdefghijklmnopqrstuvwxyz"]
print(list)
for i in range(5):
    print(random.choice(list))
