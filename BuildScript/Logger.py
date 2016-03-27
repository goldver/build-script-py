import logging
import os
import time
import glob
import logging.handlers
import inspect
import sys
import datetime

logPath = "//GENERICSERVER/Dev/Development/ProductVersions/Releases/Main_1.17/Log"
lf = "//GENERICSERVER/Dev/Development/ProductVersions/Releases/Main_1.17/Log/build"

# 2. Shows the details of every row and every function
def autolog(message):
	try:
		"Automatically log the current function details."
		# Get the previous frame in the stack, otherwise it would
		func = inspect.currentframe().f_back.f_code
		# Dump the message + the name of this function to the log.
		logging.info("%s\t\t%s:%i:\t\t%s" % ( 
			func.co_name, 
			func.co_filename, 
			func.co_firstlineno,
			message
		))
		print (message)
	except Exception, e: # catch *all* exceptions
		print( "Error: %s" % str(e) + ", please check again.")
		raise

# 1. Basic log configuration
def logSetup(verNum):
	try:
		i = datetime.datetime.now()
		logfile = lf + '_' + verNum + '.log'
		print logfile

		logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s %(message)s')

		autolog('Started')
	except Exception, e: # catch *all* exceptions
		print( "Error: %s" % str(e) + ", please check again.")
		raise
