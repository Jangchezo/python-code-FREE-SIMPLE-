# sortdic.py

# test code
"""
sortKey(dict)
sortVal(dict)
"""

dic = {}
list = ['is', 'too', 'short', 'life', 'you', 'need', 'python']

j = 0
for i in list:
    j = j+1
    dic[i] = j

# Sort by key and print them.
def sortKey(dic):    
    sortedKey = sorted(dic.keys())
    # ALSO WORKS
    # sortedKey = dic.keys()
    # sortedKey.sort()
    for item in sortedKey:
        print(item, '\t:', dic[item])
    

#Sort by value and print them.
def sortVal(dic):
    sortedVal = sorted(dic.values())
    for item in sortedVal:
        for key in dic.keys():
            if dic[key] == item:
                print(item, '\t:', key)


sortKey(dic)
print('='*50)
sortVal(dic)
    



        
