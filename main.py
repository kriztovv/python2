import random
"""#1
soucet = 0
for i in range(20):
    number = random.randint(0,99999999999999999999999999999999999999999)
    print(number)
    soucet += number
print(soucet)"""

"""#2
pocet = 0
for i in range(10):
    number = random.randint(0,99999999999999999999999999999999999999999)
    print(number)
    if number % 2 == 0:
        pocet += 1
print(pocet)"""

"""#3
randlist = []
positivelist = []
print("seznam:")
for i in range(15):
    number = random.randint(-10,10)
    print(number)
    randlist.append(number)
print("kladny seznam:")
for i in range(15):
    if randlist[i] > 0:
        print(randlist[i])
        positivelist.append(randlist[i])"""

#8
import time
randlist = []
print("seznam:")
for i in range(10):
    number = random.randint(-10,10)
    randlist.append(number)
print(randlist)
print("sorting...")
for j in range(10):
    for i in range(10 - 1):
        if randlist[i] > randlist[i + 1]:
            randlist[i], randlist[i + 1] = randlist[i + 1], randlist[i]
        print(randlist)
        time.sleep(0.1)
print("serazeny list:")
print(randlist)
        
        


    










