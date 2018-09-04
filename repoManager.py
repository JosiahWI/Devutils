import sys
import os
import settingsParser

gitHubName = "qub3d"
settingsFileName = "repoSettings.txt"


if len(sys.argv) > 1:
	gitHubName = argv[1]
	if len(sys.argv) > 2:
		settingsFileName = argv[2]
		
sourceURL = "https://github.com/" + gitHubName + "/"

#Back up one directory


settingsFile = settingsParser.Parser(settingsFileName, sourceURL)

#Back up one directory *after* initiating the parser, otherwise parser won't find the settings file
newDir = str( os.path.dirname( os.path.realpath(__file__) ) + "/../" )
os.chdir(newDir)

#Parser is an iterable object which on iteration
#returns each repo name in the settings file
#as a bash command to clone or pull it depending on whether it exists
for command in settingsFile:
	print ( command )
	os.system(command)
	