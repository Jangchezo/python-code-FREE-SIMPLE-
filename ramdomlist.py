# randomlist.py

import random

testList = list(range(10))
print(testList)

randList = []

while testList:
    try:  
        popIndex = random.randint(0, len(testList))
        popItem = testList.pop(popIndex)
        
        randList.append(popItem)

    except IndexError:
        pass
        
print(randList)
