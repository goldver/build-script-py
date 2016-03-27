import os
import sys
import shutil

from Config import *
from Logger import autolog


# Walking in every line and doing split after identification "=" and writing verNum
def configVersionUpdate(path, strVer, verNum):
	try:

		file = open(path, 'r')
		newFile = open(path + 'Temp', 'w')	

		for line in file:
			if any(substring in line for substring in strVer):
				strings = line.split('=')
				newFile.write(strings[0] + "=" + verNum + '\n')
			else:
				newFile.write(line)

		file.close()
		newFile.close()
		shutil.move(path + 'Temp', path)

	except Exception, e: # catch *all* exceptions
		autolog("Error: %s" % str(e) + ", please check again.")
		raise

# Walking into derictory and looking for all files with .iss extension. After this, changes version up to date.
def changeIss(projectPath, verNum, buildScripts):
	try:
		autolog("New version updating in ISS files is starting.")

		path = projectPath + buildScripts

		strVer = ['AppVersion', 'VersionInfoVersion', 'VersionInfoProductVersion']
		for subdir, dirs, files in os.walk(path):
			for file in files:
				fileName, fileExtension = os.path.splitext(file)
				if fileExtension == '.iss':
					autolog(path+file)
					configVersionUpdate(path+file, strVer, verNum)

		autolog("New version updating in ISS files is done.")

	except Exception, e: # catch *all* exceptions
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

sonarPath = 'Dev Project/Dev/Client/sonar-project.properties'

# Walking into derictory and looking for Sonar file. After this, changes version up to date.
def changeSonar(projectPath, verNum):
	try:
		autolog("New version updating in Sonar file is starting.")

		path = projectPath + sonarPath
		strVer = ['sonar.projectVersion']
		configVersionUpdate(path, strVer, verNum)
		autolog(path);

		autolog("New version updating in Sonar file is done.")

	except Exception, e: # catch *all* exceptions
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise


