import os
import sys
import shutil

from Config import *
from Logger import autolog, logSetup
from VersionInfoFileUpdate import createVerInfo
from InosetupAndSonarUpdate import changeIss, changeSonar
from TFScommands import getLatestVersion, pendingCheckout, checkInAfterVersionChanging 

def changeVersion():
	try:
		# Todo: remove when connecting to main
		logSetup(verNum)

		# Call from TFScommands
		getLatestVersion(localProjectPath)
		# This function checks if there are checkout local files and not permit to run script
		#pendingCheckout(localProjectPath)

		autolog("Changing version number before build is starting.");

		# Call from VersionInfoFileUpdate
		createVerInfo(localProjectPath, verNum)

		# Call from InosetupAndSonarUpdate
		changeIss(localProjectPath, verNum, buildScripts)
		changeSonar(localProjectPath, verNum)

		checkInAfterVersionChanging(localProjectPath, verNum)

		autolog("Changing version number before build is done.")

	except Exception:
		autolog('BuildScript failed :(')
		# Todo: remove when connecting to main
	#else:
	#	autolog('BuildScript succeeded :)')
	#	# To hold console 
	#finally: 
	#	print("Press any key...")
	#	sys.stdin.read()1


