#Description : Read a file

from sys import argv
filename = argv[1]
txt = open(filename)
str = txt.read()
print str
