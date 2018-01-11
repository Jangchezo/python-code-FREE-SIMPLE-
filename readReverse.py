# readReverse.py

#test code
"""
reverseRead(file)
->print from the end of the file
"""


file = open('c:/Users/JHLee/Desktop/test.txt', 'r')
lines = file.readlines()
for i in range(0, len(lines)):
      print(lines[len(lines)-i-1][0:-1])


# Real code 1

file = open('c:/Users/JHLee/Desktop/test.txt', 'r')
def reverseRead(file):
      lines = file.readlines()
      for i in range(0, len(lines)):
            seeLine = lines[len(lines)-i-1][0:-1]
            print(seeLine)

# Real code 2

file = open('c:/Users/JHLee/Desktop/test.txt', 'r')
def reverseRead(file):
      lines = file.readlines()
      lines = lines.reverse()  # WOW! It's simple.
      for seeLine in lines:
            print(seeLine)
