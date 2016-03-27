import subprocess 
import shlex
import time
import os
import shutil
import glob

from Config import *
from Logger import autolog
from subprocess import Popen, PIPE

cmdBuild = 'TFSBuild start http://ibuild:8080/tfs/Dev "Dev Project" "Dev Releases" /droplocation:\\\\IBUILD\\LatestReleases'
cmdBuildDashboard = 'TFSBuild start http://ibuild:8080/tfs/Dev "Dev Project" "Dashboard nightly build" /droplocation:\\\\IBUILD\\LatestReleases'

strBuild = 'Succeeded'

#srcPathDev = '//ibuild/LatestReleases/Dev Releases/Dev Releases '
srcPathDashboard = '//ibuild/LatestReleases/Dashboard nightly build/Dashboard nightly '

#destPathDev = '//ibuild/LatestReleases/BeforeInnoSetup'
destPathDashboard =  '//ibuild/LatestReleases/BeforeInnoSetup'

# Builds release
def buildRelease(tfscommand, buildPath):

	try:
		autolog("executing " + tfscommand);
	
		numcomms = Popen(tfscommand, stdout=PIPE, stdin=PIPE, stderr=PIPE)
		out, err = numcomms.communicate()
		autolog(out)
		autolog(err)

		for line in err:
				if strBuild == line:
					autolog (line)
					found = True
					autolog ('Your build is succeeded')
					break
				else:
					autolog('Your build not succeeded. You can not continue your task')
					raise Exception ('TFS command was failed, please do build again')
					 
		autolog("Dev Build is finished.");
		# Separation of string - 'build number'
		start = out.find('nightly')
		autolog(start)
		start = start + len('nightly')+1
		autolog(out[start:])

		end = out.find('Succeeded')
		buildNumber = out[start:end].rstrip()

		path = buildPath + buildNumber + '/'
		autolog(path)

		return path

	except Exception, e:
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise
# Copies content from build number folder (Dashboard nightly build and Dev release)	and puts in "BeforeInnoSetup" folder 
def	copyAllContentFromLatestRelease(srcpath, destpath):
	try:
		if not os.path.isdir(srcpath):
			autolog(srcpath + ' not exists, plese check again.')

		for root, dirs, files in os.walk(srcpath):

			dest = destpath + '//' + root.replace(srcpath, '')
			if not os.path.isdir(dest):
				os.mkdir(dest)
				autolog('Directory created at: ' + dest)

			#on source path don't copy the files
			if root == srcpath:
					continue

			for f in files:
				try:
					oldLoc = root + '\\' + f
					newLoc = dest + '\\' + f
				
					if os.path.isfile(newLoc):
						os.remove(newLoc)
		
					shutil.copy2(oldLoc, newLoc)
					autolog('File ' + f + ' copied.')
					
				except IOError:
					autolog('file "' + f + '" already exists')
				continue
		autolog('############################################################## \nCopy is done successfuly!')
	except Exception, e:
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

# ReleaseMaker > initialising of setup files
def runInosetupFiles():
	try:
		autolog(buildScripts)

		for root, dirs, files in os.walk(buildScripts):

			for file in files:
				command = InnoSetupPath + r' "' +  buildScripts + '\\' + file + r'"'
				autolog(command)
				numcomms = Popen(command, stdout=PIPE, stdin=PIPE, stderr=PIPE)
				out, err = numcomms.communicate()
				autolog(out)
				autolog(err)
				autolog(numcomms.returncode)

				if numcomms.returncode == 0:
					autolog ('Your InnoSetup compilation succeded\n')
				elif numcomms.returncode == 1:
					raise IOError ('The command line parameters were invalid or an internal error occurred\n')								
				elif numcomms.returncode == 2:
					raise IOError ('Your Innosetup compilation is failed\n')

	except Exception, e:
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

def releaseMaker():
	try:
		# Builds Dev release
		#srcpath = buildRelease(cmdBuild, srcPathDev)
		# Copies content from IOSiht release folder to BeforeInnoSetup folder
		#copyAllContentFromLatestRelease(srcpath, destPathDev)
		# Builds Dashboard release
		srcpath = buildRelease(cmdBuildDashboard, srcPathDashboard)

		# Copies content from Dashboard nightly release folder to BeforeInnoSetup folder
		copyAllContentFromLatestRelease(srcpath, destPathDashboard)

		# Creates all MSIs files and puts them in output folder
		#runInosetupFiles()
	except Exception, e:
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise





