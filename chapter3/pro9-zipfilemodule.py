#import zipfile
#var=zipfile.ZipFile('exice.zip')
#print var
#for i in var.namelist():
#	iprint i
import zipfile
z = zipfile.ZipFile("exice.zip")
for name in z.namelist():
	print "FILE:", z.namelist()
	print z.read(name)
