import sys
import time
import os

watchdir = 'C:\Test'
contentse = os.listdir(watchdir)
count = len(watchdir)
dirmtime = os.stat(watchdir).st_mtime

while True:
	newmtime = os.stat(watchdir).st_mtime
	if newmtime != dirmtime:
		dirmtime = newmtime
		newcontents = os.listdir(watchdir)
		added = set(newcontents).difference(contentse)
		if added:
			print(added)
			f = open("C:\drive.txt", "a")
			f.write("\n")
			f.write("Inserted")
			f.write("\n")
			added=' '.join(added)
			f.write(added)
			f.close()
		removed = set(contentse).difference(newcontents)
		if removed:
			print(removed)
			f = open("C:\drive.txt", "a")
			f.write("\n")
			f.write("Removed")
			f.write("\n")
			removed=' '.join(removed)
			f.write(removed)
			f.close()
		contentse = newcontents
	time.sleep(2)








