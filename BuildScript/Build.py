import os
import sys
import shutil
from Config import *

from Logger import autolog, logSetup
from ChangeVersionBeforeBuild import changeVersion
from ImportFiles import copySetupFiles, removeDestDir
from PostBuildActions import changeReleaseNoteAfterCopy, changeVerFileTxtAfterCopy, changeDataBaseVersionAfterCopy, createZipAndCopyToDropbox
from ReleaseMaker import releaseMaker

try:
	
	logSetup(verNum)
	autolog("Build process is starting...");
	autolog("****************************");
	autolog("Build number:\t" + verNum);
	autolog("Local project path:\t" + localProjectPath);

	root_dst_main_dir = mainOutputDirectory + verNum

	autolog("New version directory:\t" + root_dst_main_dir);
	autolog("Configuration file:\t" + copyFilesConfig);
	autolog("****************************");

	# Uncomment ChangeVersionBeforeBuild
	changeVersion() 

	# Makes release
	releaseMaker()

	# Call from ImportFiles.py
	copySetupFiles(copyFilesConfig, root_dst_main_dir)
	
	# Call from PostBuildActions.py
	changeReleaseNoteAfterCopy(root_dst_main_dir, verNum)
	changeVerFileTxtAfterCopy(root_dst_main_dir, verNum)
	changeDataBaseVersionAfterCopy(root_dst_main_dir, verNum)
	createZipAndCopyToDropbox(root_dst_main_dir, ZipFileDestination)
	
	autolog("Build process is done...");
	autolog("****************************");

except Exception:
	autolog('BuildScript failed :(')

	# If failed, remove all destination directory
	removeDestDir(root_dst_main_dir)

else:
	autolog('BuildScript succeeded :)')
	# To hold console 
finally: 
	print("Press any key...")
	sys.stdin.read(1)
	

