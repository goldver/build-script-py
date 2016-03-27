
# Automatic deployment from 'files.conf' file

import re
import os
import shutil 
import sys

from Logger import autolog

def copySetupFiles(copyFilesConfig, root_dst_main_dir):

	try:
			autolog("New version directory creation is starting.")

			# Check if child of main folder exists. If not, do new child folder
			if not os.path.exists(root_dst_main_dir):
				   os.mkdir(root_dst_main_dir)

			# Open and read configuration file
			fp = open(copyFilesConfig, "r")

			for line in fp:
			# Skip row when Number sign (#) appears
				if not line[0]=='#':

					# Split strings in file   
					words = line.split()
					# Array creation for split
					sourceDir = words[0]
					sourceFile = words[1]
					destDir = words[2]
					destFile = words[3]

					# Base directory creation
					baseDir = root_dst_main_dir;
					for x in destDir.split('/'):
						baseDir = baseDir + '/' + x
						if not os.path.exists(baseDir):
							os.mkdir(baseDir)
					src = sourceDir + "/" + sourceFile
					dst = root_dst_main_dir + "/" + destDir + "/" + destFile
					autolog("copy from: " + src)
					autolog("copy to:" + dst)

					# Copying files into directories
					shutil.copyfile(src, dst)

					autolog("New version directory creation is done.")

	except Exception, e: # catch *all* exceptions
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

def removeDestDir(root_dst_main_dir):
	try:
		if not os.path.exists( root_dst_main_dir):
			shutil.rmtree(root_dst_main_dir)
			autolog("Destination directory removed!")

	except Exception, e: # catch *all* exceptions
		autolog("Error: %s" % str(e) + ", please check again.")
		raise
