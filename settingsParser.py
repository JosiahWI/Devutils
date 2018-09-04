import os

class Parser:
	
	def __init__(self, settingsFileName, sourceRepo):
		self.sourceRepo = sourceRepo
		settingsFile = open(settingsFileName, "rb")
		self.commandList = [self.parseCommand(line) for line in settingsFile]
		settingsFile.close()
		
	def __iter__(self):
		#n starts at -1 because in self.next() it gets incremented before we return, not after
		self.n = -1
		return self
		
	#Python3 looks for the __next__() function.
	def __next__(self):
		try:
			self.n += 1
			return self.commandList[self.n]
		except IndexError:
			raise StopIteration
	
	#Python2 looks for a next() function.
	def next(self):
		return self.__next__()
			
	def parseCommand(self, line):
		#Python3 will not implicitly convert a file line to str, must be done manually.
		#There might be a better way to do this, as this way we have to cut out the first part
		line = str(line.strip())
		if line[0] == 'b':
			line = line[2:-1]
		#Is the line a comment, return an empty command
		if line[0] == "#":
			return (("", ""))
		#If the directory exists, return a git pull command.
		if os.path.isdir(line):
			return (("git pull"), line)
		else:
			return (("git clone " + self.sourceRepo + line), line)
		
		