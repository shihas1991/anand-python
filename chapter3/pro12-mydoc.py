#Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.
import sys
__import__(sys.argv[1])
print 'Help on module',sys.argv[1]
print '\n\n\nDESCRIPTION\n\n\n'
print __import__(sys.argv[1]).__doc__
print '\n\n\nFUNCTIONS\n\n\n'
for i in dir(sys.argv[1]):
	print i,()
