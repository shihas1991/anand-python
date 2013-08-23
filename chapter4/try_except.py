#import os
#try:
#	os.mkdir('shihas')
#except:print 'file not exist'
#def main():
#    filename = sys.argv[1]
#    try:
#        for row in parse_csv(filename):
#            print row
#    except IOError:
#        print >> sys.stderr, "The given file doesn't exist: ", filename
#        sys.exit(1)
#try:
#    os.mkdir('shihas')
#except IOError, e:
#    print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
#    sys.exit(1)
#except FormatError, e:
#    print >> sys.stderr, "File is badly formatted (%s): %s" % (str(e), filename)
try:
    print "a"
except:
    print "b"
else:
    print "c"
finally:
    print "d"
print '\n\n\n\n'
try:
    print "a"
    raise Exception("doom")
except:
    print "b"
else:
    print "c"
finally:
    print "d"
print '\n\n\n'
def f():
    try:
        print "a"
        return
    except:
        print "b"
    else:
        print "c"
    finally:
        print "d"

f()

