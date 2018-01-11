# tab2Space.py
"""
Input & Output
==============
foo(fp)
file with 4 spaces
"""

# Solution 1
old = open('c:/Users/JHLee/Desktop/test2.txt', 'r')
lines = old.readlines()
old.close()

new = open('c:/Users/JHLee/Desktop/test3.txt', 'w')
for line in lines:
      line = line.replace('\t', '    ')
      new.write(line)
new.close()

# Solution 2
import sys

def usage():
      print(
      """
      Usage
      =====
      %s -v : view the file
      %s -c : change the file
      """ % (sys.argv[1], sys.argv[1]))

file = sys.argv[1]

if not sys.argv[2:] or sys.argv[2] not in ['-v', '-c']:
      usage()
elif sys.argv[2] == '-v':
      try:
            fp = open(file, 'r')
            data = fp.read()
            print(data)
      except IOError:
            print('ERROR : No such file!')
elif sys.argv[2] == '-c':
      try:
            fpOld = open(file, 'r')
            text = fpOld.readlines()
            fpOld.close()

            fpNew = open('c:/Users/JHLee/Desktop/test4.txt', 'w')
            for line in text:
                  line = line.replace('\t', '    ')
                  fpNew.write(line)
            fpNew.close()

            print('New file is generated.')
      except IOError:
            print('ERROR: No such file!')


