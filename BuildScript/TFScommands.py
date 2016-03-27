import subprocess 
import shlex
import time
import tempfile
import os

from Config import *
from Logger import autolog

# Need to add the tf.exe path (c:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\IDE\) to the PATH variable
cmdGet = 'tf.exe get'
cmdStat = 'tf.exe stat'
cmdCheckIn = 'tf.exe checkin /noprompt /comment:'

DevPath = 'Dev Project/Dev'

# Get latest version command
def getLatestVersion(projectPath):
	
	try:
		autolog("Getting latest version is starting.");

		path = projectPath + DevPath
																								   
		child = subprocess.Popen(shlex.split(cmdGet), shell=False, stdout=subprocess.PIPE, cwd=path); 

		out, err = child.communicate();

		autolog("Getting latest version in is done sccesfully!");

	except Exception, e:
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

######################################################################################

# Checks if exists any local file in check out state. If yes, you must check in any local file 
def pendingCheckout(projectPath):
	
	try:
		autolog("Stat version is starting.");

		path = projectPath + DevPath


		w = "test.txt"
		f = open("test.txt","a")																					   
		strCheckout = 'There are no pending changes.'

		p = subprocess.Popen(shlex.split(cmdStat), cwd=path, shell=True, stdout=f,
			stderr=subprocess.STDOUT, bufsize=0)

		for x in range(0, 5):
			time.sleep(1)
			print(x)

		# Closes test.txt in case of crushes
		with open("test.txt", 'r') as r:

			found = False

			for line in r:
				if strCheckout == line:
					autolog (line)
					found = True
					if (found == False):
						autolog ('You have an unchecked files. Please do check in and run script again.')
				else:
					print 'You have an unchecked files. Please do check in and run script again.' 
					f.close()
					raise Exception('Dear user')
		# Closes test.txt 
		f.close()

		autolog("Stat version is done saccesfully!");
				
	except Exception, e:
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise
			
#############################################################################

# After changing of version number in files (*.ISS, VersionInfo) does check in 
def checkInAfterVersionChanging(projectPath, verNum):
	
	try:
		autolog("Check in is starting.");
		# Flag of with check in/without check in
		if (DoCheckIn):
			runCmd = cmdCheckIn + '\"Automatic build for version "' + verNum + "\""
			
			path = projectPath + DevPath
																								   
			child = subprocess.Popen(shlex.split(cmdCheckIn), shell=False, stderr=subprocess.PIPE, cwd=path);
			 
			out, err = child.communicate();

			for x in range(0, 150):
				time.sleep(1)
				print(x)

			autolog ("Out:");
			autolog (out);
			autolog ("error:");
			autolog (err);
		else:
			autolog("Not checking in");

		autolog("Check in is done sccesfully!");
				
	except Exception, e: # catch *all* exceptions
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

############################################################################








