import os
import sys
import shutil

from Logger import autolog

path ='Dev Project/Dev/Common/Dev.Info/VersionInfo.cs'

# Changes version number in AssemblyVersion file by spliting it to 3 strings 
str1 = '''using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Build and Revision Numbers
// by using the '*' as shown below:

[assembly: AssemblyVersion("'''

str2 = '''")]
[assembly: AssemblyFileVersion("'''
						  
str3 = '")]'

def createVerInfo(projectPath, version):

	autolog("Changing VersionInfo.cs is starting.")

	try:
		FullfilePath = projectPath + path 
		csfile = str1 + version + str2 + version + str3
		autolog(csfile)
		text_file = open(FullfilePath, "w")
		text_file.write(csfile)
		text_file.close()

		autolog("Changing VersionInfo.cs is done.")

	except Exception, e: # catch *all* exceptions
		autolog("Error: %s" % str(e) + ", please check again.")
		raise
	
