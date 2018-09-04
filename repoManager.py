import sys
import os
import settingsParser



#Set the root directory and change into it
rootDir = str( os.path.dirname( os.path.realpath(__file__) ) + "/../" )
os.chdir(rootDir)

gitHubName = "qub3d"
settingsFileName = rootDir + "/devutils/repoSettings.txt"

#Check command line options
if len(sys.argv) > 1:
	gitHubName = sys.argv[1]
	if len(sys.argv) > 2:
		settingsFileName = rootDir + "/devutils/" + sys.argv[2]
	
#Create a workspace if it hasn't been already, and change into it.
#This also sets up the workspace that settingsParser will use to check for existing repos.
if not os.path.isdir(gitHubName):
	os.mkdir(gitHubName)
userDir = rootDir + gitHubName
os.chdir(userDir)

sourceURL = "https://github.com/" + gitHubName + "/"

settingsFile = settingsParser.Parser(settingsFileName, sourceURL)



#Parser is an iterable object which on iteration
#returns each repo name in the settings file
#as a bash command to clone or pull it depending on whether it exists
for command, repoName in settingsFile:
	print ( command )
	print ( command + " : " + gitHubName + "/" + repoName )
	#If the command is a pull, change into the directory to be pulled, pull and then change back.
	if command[0:8] == "git pull":
		os.chdir(userDir + "/" + repoName)
		os.system(command)
		os.chdir(userDir)
	else:
		os.system(command)
	