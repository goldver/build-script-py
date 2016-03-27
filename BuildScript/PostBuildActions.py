import re
import os
import sys
import shutil
import zipfile

from Logger import autolog

# Changing content of ReleaseNote.txt file after copying from source
def changeReleaseNoteAfterCopy(root_dst_main_dir, verNum):

	try:
		autolog("Release note file creation is starting.")

		RelNoteFile	= root_dst_main_dir + '/Resource/ReleaseNotes.txt'

		f = open(RelNoteFile,'r+')
		f.truncate()
		f.write('Relase notes for version ' + verNum) 
		f.close 

		autolog("Release note file creation is done.")

	except Exception, e: # catch *all* exceptions
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

# Changing content of versionFile.txt file after copying from source
def changeVerFileTxtAfterCopy(root_dst_main_dir, verNum):

	try:
		autolog("Version file creation is starting.")

		verFile = root_dst_main_dir + '/Resource/version.txt'

		f = open(verFile,'r+')
		f.truncate()
		f.write(verNum) 
		f.close

		autolog("Version note file creation is starting.")

	except Exception, e: # catch *all* exceptions
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

# Changing base.back file after copying from source (SQL Server 2008r2 ib iBuild wuth daily job)						
def changeDataBaseVersionAfterCopy(root_dst_main_dir, verNum):
	base = root_dst_main_dir + '/Resource/'

	try:
		autolog("Data base file moving is starting.")

		os.rename(base + 'base.bak', base + 'base_' + verNum  + '.bak')

		autolog("Data base file moving is done.")

	except Exception, e: # catch *all* exceptions
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise

# Creating Zip file and put it to some destination (Dropbox, for example)
def createZipAndCopyToDropbox(root_dst_main_dir, ZipFileDestination):

	zipFile = root_dst_main_dir + '.zip'

	try:
		# Create ZIP file
		autolog('ZIP file creation is starting...')

		zf = zipfile.ZipFile(zipFile, "w")
		for dirname, subdirs, files in os.walk(root_dst_main_dir):

			zf.write(dirname)
			for filename in files:
				zf.write(os.path.join(dirname, filename))
		zf.close()

		autolog('Zip file creation is done!')

		# Put directory to some destination folder (Dropbox, for example)
		autolog('Transfering Zip file to destination folder is starting...')

		shutil.move(zipFile, ZipFileDestination)
		autolog('Your Zip is ready in destination folder.')

	except Exception, e: # catch *all* exceptions
		autolog( "Error: %s" % str(e) + ", please check again.")
		raise